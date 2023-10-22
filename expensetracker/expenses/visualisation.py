from django.conf import settings
import matplotlib.pyplot as plt
from pathlib import Path
import numpy as np
import time


def formatData(data):
    category_totals_dict = {}
    for category_info in data:
        category_name = category_info['category__name']
        distribution_expense = category_info['distribution_expense']
        category_totals_dict[category_name] = distribution_expense
    return category_totals_dict


def charts(data):
    formated_data = formatData(data=data)
    charts_file_name = f"chart_{time.time()}.png"
    path = Path(settings.BASE_DIR / "static" / "expenses" / "images" / charts_file_name)
    plt.style.use('_mpl-gallery-nogrid')
    colors = plt.get_cmap('tab20')(np.linspace(0.1, 0.9, len(data)))
    fig, ax = plt.subplots(figsize=(5, 5))
    values = tuple(formated_data.values())
    labels = tuple(formated_data.keys())
    ax.pie(values, labels=labels, colors=colors, radius=3, center=(4, 4),
           wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame=False,
           pctdistance=0, normalize=True, labeldistance=None)
    ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
           ylim=(0, 8), yticks=np.arange(1, 8))
    plt.legend()
    plt.savefig(path, format="png")
    return charts_file_name
