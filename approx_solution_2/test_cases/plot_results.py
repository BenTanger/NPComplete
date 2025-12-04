#!/usr/bin/env python3
"""Parse `output.txt` produced by the test runner and plot Cost and Runtime vs problem size.

Usage:
  python3 plot_results.py --input output.txt --out-dir plots --show

Produces PNG files in `--out-dir` (default `plots`) and optionally shows them.
"""

import argparse
import os
import re
from collections import defaultdict, OrderedDict

import matplotlib.pyplot as plt


def parse_output(path):
	with open(path, 'r') as f:
		data = f.read().strip()

	# split into blocks separated by blank lines
	blocks = [b.strip() for b in data.split('\n\n') if b.strip()]

	entries = []
	for b in blocks:
		lines = b.splitlines()
		d = {}
		for line in lines:
			if line.startswith('Test:'):
				d['test'] = line.split(':', 1)[1].strip()
			elif line.startswith('Cost:'):
				d['cost'] = float(line.split(':', 1)[1].strip())
			elif line.startswith('Path:'):
				path_str = line.split(':', 1)[1].strip()
				tokens = path_str.split()
				# if path is closed (first == last), treat n = len(tokens)-1
				if len(tokens) >= 2 and tokens[0] == tokens[-1]:
					d['path'] = tokens
					d['n'] = len(tokens) - 1
				else:
					d['path'] = tokens
					d['n'] = len(tokens)
			elif line.startswith('Runtime:'):
				# extract float
				m = re.search(r'([0-9]*\.?[0-9]+)', line)
				d['runtime'] = float(m.group(1)) if m else None
		# if n not found, try to infer from filename in test
		if 'n' not in d and 'test' in d:
			m = re.search(r'_([0-9]+)\.txt$', d['test'])
			if m:
				d['n'] = int(m.group(1))
		# also extract group (first/second/...)
		if 'test' in d:
			parts = d['test'].split('/')
			if len(parts) >= 2:
				d['group'] = parts[0]
			else:
				d['group'] = ''
		entries.append(d)

	return entries


def aggregate(entries):
	# structure: group -> OrderedDict(n -> list of values)
	groups_cost = defaultdict(lambda: defaultdict(list))
	groups_rt = defaultdict(lambda: defaultdict(list))

	for e in entries:
		g = e.get('group', '')
		n = e.get('n')
		if n is None:
			continue
		if 'cost' in e:
			groups_cost[g][n].append(e['cost'])
		if 'runtime' in e:
			groups_rt[g][n].append(e['runtime'])

	# convert to sorted OrderedDict per group
	for g in list(groups_cost.keys()):
		groups_cost[g] = OrderedDict(sorted((k, groups_cost[g][k]) for k in groups_cost[g]))
	for g in list(groups_rt.keys()):
		groups_rt[g] = OrderedDict(sorted((k, groups_rt[g][k]) for k in groups_rt[g]))

	return groups_cost, groups_rt


def compute_overall_avg(groups):
	"""Given groups dict (group -> OrderedDict(n -> list(vals))) return OrderedDict(n -> avg)
	combining across all groups."""
	overall = defaultdict(list)
	for g, d in groups.items():
		for n, vals in d.items():
			overall[n].extend(vals)
	if not overall:
		return OrderedDict()
	return OrderedDict(sorted((n, sum(vals) / len(vals)) for n, vals in overall.items()))


def plot_groups(groups_cost, groups_rt, out_dir, show=False, series=None):
	"""Plot overall average per series.

	series: list of tuples (label, groups_cost, groups_rt)
	If series is None, default is one series using provided groups_cost/groups_rt.
	"""
	os.makedirs(out_dir, exist_ok=True)

	if series is None:
		series = [('data', groups_cost, groups_rt)]

	# Prepare color cycle
	colors = plt.rcParams['axes.prop_cycle'].by_key().get('color', ['black', 'red', 'blue', 'green'])

	# COST plot: one line per series
	plt.figure(figsize=(8, 5))
	for idx, (label, gcost, grt) in enumerate(series):
		avg_cost = compute_overall_avg(gcost)
		if not avg_cost:
			continue
		xs = list(avg_cost.keys())
		ys = list(avg_cost.values())
		plt.plot(xs, ys, marker='o', linestyle='-', color=colors[idx % len(colors)], label=label)
	plt.xlabel('n (problem size)')
	plt.ylabel('Cost (average over tests)')
	plt.title('TSP: Average Cost vs n (comparison)')
	plt.legend()
	plt.grid(True)
	out = os.path.join(out_dir, 'cost_compare_avg_vs_n.png')
	plt.tight_layout()
	plt.savefig(out)
	if show:
		plt.show()
	plt.close()

	# RUNTIME plot
	plt.figure(figsize=(8, 5))
	for idx, (label, gcost, grt) in enumerate(series):
		avg_rt = compute_overall_avg(grt)
		if not avg_rt:
			continue
		xs = list(avg_rt.keys())
		ys = list(avg_rt.values())
		plt.plot(xs, ys, marker='o', linestyle='-', color=colors[idx % len(colors)], label=label)
	plt.xlabel('n (problem size)')
	plt.ylabel('Runtime (seconds, average)')
	plt.title('TSP: Average Runtime vs n (comparison)')
	plt.legend()
	plt.grid(True)
	out = os.path.join(out_dir, 'runtime_compare_avg_vs_n.png')
	plt.tight_layout()
	plt.savefig(out)
	if show:
		plt.show()
	plt.close()


def main():
	parser = argparse.ArgumentParser(description='Plot results from output.txt')
	parser.add_argument('--input', '-i', action='append', help='path to output.txt. Can be given multiple times. Use label:path to name series.')
	parser.add_argument('--out-dir', '-o', default='plots', help='output directory for PNGs')
	parser.add_argument('--show', action='store_true', help='show plots interactively')
	parser.add_argument('--csv', default=None, help='optional path to write combined CSV of averages')
	args = parser.parse_args()
	inputs = args.input or ['output.txt']

	series = []
	script_dir = os.path.dirname(__file__)
	for inp in inputs:
		label = None
		path = inp
		if ':' in inp:
			label, path = inp.split(':', 1)
		# resolve path relative to script dir if needed
		if not os.path.exists(path):
			alt = os.path.join(script_dir, path)
			if os.path.exists(alt):
				path = alt
		if not os.path.exists(path):
			print(f'Warning: input file not found: {inp} (resolved to {path}), skipping')
			continue
		entries = parse_output(path)
		groups_cost, groups_rt = aggregate(entries)
		if not label:
			# infer label from parent dir or filename
			b = os.path.basename(os.path.dirname(path))
			if b == '' or b == '.':
				b = os.path.splitext(os.path.basename(path))[0]
			label = b
		series.append((label, groups_cost, groups_rt))

	if not series:
		print('No valid input files found. Exiting.')
		return

	plot_groups(None, None, args.out_dir, show=args.show, series=series)

	# Optionally write combined CSV of averages
	if args.csv:
		# collect union of n across all series
		all_ns = set()
		series_cost_avgs = {}
		series_rt_avgs = {}
		for label, gcost, grt in series:
			ca = compute_overall_avg(gcost)
			ra = compute_overall_avg(grt)
			series_cost_avgs[label] = ca
			series_rt_avgs[label] = ra
			all_ns.update(ca.keys())
			all_ns.update(ra.keys())
		ns = sorted(all_ns)
		# write CSV header
		with open(args.csv, 'w') as outf:
			header = ['n']
			for label in [s[0] for s in series]:
				header.append(f'{label}_cost')
				header.append(f'{label}_runtime')
			outf.write(','.join(header) + '\n')
			for n in ns:
				row = [str(n)]
				for label in [s[0] for s in series]:
					cost_avg = series_cost_avgs.get(label, {}).get(n, '')
					rt_avg = series_rt_avgs.get(label, {}).get(n, '')
					row.append(str(cost_avg) if cost_avg != '' else '')
					row.append(str(rt_avg) if rt_avg != '' else '')
				outf.write(','.join(row) + '\n')
		print('CSV written to', args.csv)

	print('Plots written to', args.out_dir)


if __name__ == '__main__':
	main()

