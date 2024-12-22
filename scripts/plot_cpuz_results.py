import matplotlib.pyplot as plt

labels = ["no VMI", "CR3 monitoring"]
values = [334.7, 259.9]

plt.bar(labels, values, color=['blue', 'orange'])

plt.ylabel('CPU-Z Score')

plt.savefig("plots/impact_cr3_monitoring.pdf", format="pdf")

plt.close()
