import matplotlib.pyplot as plt
import numpy as np
import csv

def read_files_and_plot_box(files, plot_filename, ylimit, textoffset, figsize, fontsize, scaling, unit):
    data = []
    labels = []

    for filename, label in files:
        with open(filename, 'r') as f:
            numbers = [float(line.strip()) / scaling for line in f if line.strip().isdigit()]
            if numbers:
                data.append(numbers)
                labels.append(label)
            else:
                print(f"No valid numbers found in {filename}")

    plt.rcParams.update({'font.size': fontsize})
    plt.figure(figsize=figsize)
    plt.boxplot(data, labels=labels)
    for i, dataset in enumerate(data, 1):
        median = np.median(dataset)
        plt.text(i+textoffset, median, f'{median:.2f} {unit}', horizontalalignment='left', verticalalignment='center', color='black')
    plt.ylim(ylimit)
    plt.xticks(rotation=45)
    plt.xlabel('Workload')
    plt.ylabel(f'Latency [{unit}]')
    plt.tight_layout()
    plt.savefig(plot_filename, format="pdf")
    plt.close()

files_no_vmi = [
    ('results/result_2024-12-22_01-03-58_no-vmi/timing_overhead.csv', 'timer'),
    ('results/result_2024-12-22_01-03-58_no-vmi/exec_bp_only.csv', 'exec bp'),
    ('results/result_2024-12-22_01-03-58_no-vmi/exec_page.csv', 'exec page'),
    ('results/result_2024-12-22_01-03-58_no-vmi/read_byte.csv', 'read byte'),
    ('results/result_2024-12-22_01-03-58_no-vmi/read_page.csv', 'read page'),
]
read_files_and_plot_box(files_no_vmi, "plots/execread_boxplot_no_vmi.pdf", (0, 10), 0.28, (10, 6), 13, 1000, "\u03bcs")

files_vmi = [
    ('results/result_2024-12-22_01-04-11_vmi/timing_overhead.csv', 'timer'),
    ('results/result_2024-12-22_01-04-11_vmi/exec_bp_only.csv', 'exec bp'),
    ('results/result_2024-12-22_01-04-11_vmi/exec_page.csv', 'exec page'),
    ('results/result_2024-12-22_01-04-11_vmi/read_byte.csv', 'read byte'),
]
read_files_and_plot_box(files_vmi, "plots/execread_boxplot_vmi.pdf", (0, 100), 0.24, (10,6), 13, 1000, "\u03bcs")

files_vmi_page = [
    ('results/result_2024-12-22_01-04-11_vmi/read_page.csv', 'read page'),
]
read_files_and_plot_box(files_vmi_page, "plots/execread_boxplot_vmi_readpage.pdf", (20, 30), 0.1, (6, 6), 13, 1000000, "ms")
