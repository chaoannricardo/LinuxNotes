#! /usr/bin/env python
# coding=utf-8
# Copyright (c) 2019 Uber Technologies, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
# ==============================================================================
# [3rd-Party Modification Disclaimation]
# This is a 3rd-Party modification based on original code!!!
# Original Repository: https://github.com/uber/ludwig
# Original Document: https://github.com/uber/ludwig/blob/master/ludwig/utils/visualization_utils.py 
# Last Modified: 04/28/19
# Maintainer: Ricardo S. Chao;https://www.linkedin.com/in/chaoannricardo/; https://github.com/chaoannricardo
# Modifications:
# >>>Added "plt.savefig(title+'.png')" before each "plt.show()" to enable saving graphs.
# ==============================================================================

from __future__ import absolute_import
from __future__ import division

from collections import Counter
from sys import platform

import copy
import logging
import matplotlib as mpl

if platform == "darwin":  # OS X
    mpl.use('TkAgg')
import matplotlib.patches as patches
import matplotlib.path as path
import matplotlib.patheffects as PathEffects
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib import ticker
from matplotlib.lines import Line2D
from mpl_toolkits.mplot3d import Axes3D

import ludwig.contrib

# plt.rc('xtick', labelsize='x-large')
# plt.rc('ytick', labelsize='x-large')
# plt.rc('axes', labelsize='x-large')

def learning_curves_plot(train_values, vali_values, metric, algorithm_names=None,
                        title=None):
    num_algorithms = len(train_values)
    max_len = max([len(tv) for tv in train_values])

    fig, ax = plt.subplots()

    sns.set_style('whitegrid')

    if title is not None:
        ax.set_title(title)

    if num_algorithms == 1:
        colors = plt.get_cmap('tab10').colors
    else:  # num_algorithms > 1
        colors = plt.get_cmap('tab20').colors

    ax.grid(which='both')
    ax.grid(which='minor', alpha=0.5)
    ax.grid(which='major', alpha=0.75)
    ax.set_xlabel('epochs')
    ax.set_ylabel(metric.replace('_', ' '))

    xs = list(range(1, max_len + 1))

    for i in range(num_algorithms):
        name_prefix = algorithm_names[
                          i] + ' ' if algorithm_names is not None and i < len(
            algorithm_names) else ''
        ax.plot(xs, train_values[i], label=name_prefix + 'training',
                color=colors[i * 2], linewidth=3)
        if i < len(vali_values):
            ax.plot(xs, vali_values[i], label=name_prefix + 'validation',
                    color=colors[i * 2 + 1], linewidth=3)

    ax.legend()
    plt.tight_layout()
    ludwig.contrib.contrib_command("visualize_figure", plt.gcf())
    plt.savefig(title+'.png')
    plt.show()


def compare_classifiers_plot(scores, metrics, algoritm_names=None,
                             adaptive=False, decimals=4, title=None):
    assert len(scores) == len(metrics)
    assert len(scores) > 0

    num_metrics = len(metrics)

    sns.set_style('whitegrid')

    fig, ax = plt.subplots()

    ax.grid(which='both')
    ax.grid(which='minor', alpha=0.5)
    ax.grid(which='major', alpha=0.75)
    ax.set_xticklabels([], minor=True)

    if title is not None:
        ax.set_title(title)

    width = 0.8 / num_metrics if num_metrics > 1 else 0.4
    ticks = np.arange(len(scores[0]))

    colors = plt.get_cmap('tab10').colors
    if adaptive:
        maximum = max([max(score) for score in scores])
    else:
        ax.set_xlim([0, 1])
        ax.set_xticks(np.linspace(0.0, 1.0, num=21), minor=True)
        ax.set_xticks(np.linspace(0.0, 1.0, num=11))
        maximum = 1

    half_total_width = 0.4 if num_metrics > 1 else 0.2
    ax.set_yticks(ticks + half_total_width - width / 2)
    ax.set_yticklabels(algoritm_names if algoritm_names is not None else '')
    ax.invert_yaxis()  # labels read top-to-bottom

    for i, metric in enumerate(metrics):
        ax.barh(ticks + (i * width), scores[i], width, label=metric,
                color=colors[i])

        for j, v in enumerate(scores[i]):
            if v < maximum * (0.025 * decimals + 0.1):
                x = v + maximum * 0.01
                horizontal_alignment = 'left'
            else:
                x = v - maximum * 0.01
                horizontal_alignment = 'right'
            txt = ax.text(x, ticks[j] + (i * width),
                          ('{:.' + str(decimals) + 'f}').format(v),
                          color='white',
                          fontweight='bold', verticalalignment='center',
                          horizontalalignment=horizontal_alignment)
            txt.set_path_effects(
                [PathEffects.withStroke(linewidth=3, foreground='black')])

    plt.setp(ax.get_xminorticklabels(), visible=False)

    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.tight_layout()
    ludwig.contrib.contrib_command("visualize_figure", plt.gcf())
    plt.savefig(title+'.png')
    plt.show()


def compare_classifiers_line_plot(xs, scores, metric, algorithm_names=None,
                                  title=None):
    sns.set_style('whitegrid')
    colors = plt.get_cmap('tab10').colors

    fig, ax = plt.subplots()

    ax.grid(which='both')
    ax.grid(which='minor', alpha=0.5)
    ax.grid(which='major', alpha=0.75)

    if title is not None:
        ax.set_title(title)

    ax.set_xticks(xs)
    ax.set_xticklabels(xs)
    ax.set_xlabel('k')
    ax.set_ylabel(metric)

    for i, score in enumerate(scores):
        ax.plot(xs, score,
                label=algorithm_names[
                    i] if algorithm_names is not None and i < len(
                    algorithm_names) else 'Algorithm {}'.format(i),
                color=colors[i], linewidth=3, marker='o')

    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.tight_layout()
    ludwig.contrib.contrib_command("visualize_figure", plt.gcf())
    plt.savefig(title+'.png')
    plt.show()


def compare_classifiers_multiclass_multimetric_plot(scores, metrics,
                                                    labels=None, title=None):
    assert len(scores) > 0

    sns.set_style('whitegrid')

    fig, ax = plt.subplots()

    if title is not None:
        ax.set_title(title)

    width = 0.9 / len(scores)
    ticks = np.arange(len(scores[0]))

    colors = plt.get_cmap('tab10').colors
    ax.set_xlabel('class')
    ax.set_xticks(ticks + width)
    if labels is not None:
        ax.set_xticklabels(labels, rotation=90)
    else:
        ax.set_xticklabels(ticks, rotation=90)

    for i, score in enumerate(scores):
        ax.bar(ticks + i * width, score, width, label=metrics[i],
               color=colors[i])

    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.tight_layout()
    ludwig.contrib.contrib_command("visualize_figure", plt.gcf())
    plt.savefig(title+'.png')
    plt.show()


def radar_chart(ground_truth, predictions, algorithms=None, log_scale=False,
                title=None):
    sns.set_style('whitegrid')

    if title is not None:
        plt.title(title)

    ground_truth = ground_truth[0:10]
    predictions = [pred[0:10] for pred in predictions]

    gt_argsort = np.argsort(-ground_truth)  # sort deacreasing
    logging.info(gt_argsort)
    ground_truth = ground_truth[gt_argsort]
    predictions = [pred[gt_argsort] for pred in predictions]

    maximum = max(max(ground_truth), max([max(p) for p in predictions]))

    ax = plt.subplot(111, polar=True)
    ax.set_theta_zero_location('N')
    ax.set_theta_direction(-1)
    ax.set_rmax(maximum)
    ax.set_rlabel_position(305)
    ax.set_ylabel('Probability')
    # ax.set_rscale('log')
    ax.grid(True)

    colors = plt.get_cmap('tab10').colors

    num_classes = len(ground_truth)

    # Set ticks to the number of properties (in radians)
    t = np.arange(0, 2 * np.pi, 2 * np.pi / num_classes)
    ax.set_xticks(t, [])
    ax.set_xticklabels(np.arange(0, num_classes))

    # Set yticks from 0 to 10
    # ax.set_yticks(np.linspace(0, 10, 11))
    # Set axes limits
    # ax.set_rlim(0, 1)
    # ax.set_rscale('log')

    def draw_polygon(values, label, color='grey'):
        points = [(x, y) for x, y in zip(t, values)]
        points.append(points[0])
        points = np.array(points)

        codes = [path.Path.MOVETO, ] + \
                [path.Path.LINETO, ] * (len(values) - 1) + \
                [path.Path.CLOSEPOLY]
        _path = path.Path(points, codes)
        _patch = patches.PathPatch(_path, fill=True, color=color, linewidth=0,
                                   alpha=.2)
        ax.add_patch(_patch)
        _patch = patches.PathPatch(_path, fill=False, color=color, linewidth=3)
        ax.add_patch(_patch)

        # Draw circles at value points
        # line = ax.scatter(points[:, 0], points[:, 1], linewidth=3,
        #            s=50, color='white', edgecolor=color, zorder=10)
        ax.plot(points[:, 0], points[:, 1], linewidth=3, marker='o',
                fillstyle='full',
                markerfacecolor='white',
                markeredgecolor=color,
                markeredgewidth=2,
                color=color, zorder=10, label=label)

    draw_polygon(ground_truth, 'Ground Truth')

    # Draw polygon representing values
    for i, alg_predictions in enumerate(predictions):
        draw_polygon(alg_predictions, algorithms[i], colors[i])

    ax.legend(frameon=True, loc='upper left')
    plt.tight_layout()
    ludwig.contrib.contrib_command("visualize_figure", plt.gcf())
    plt.savefig(title+'.png')
    plt.show()


def pie(ax, values, **kwargs):
    total = sum(values)

    def formatter(pct):
        if pct > 0:
            return '{:0.0f}\n({:0.1f}%)'.format(pct * total / 100, pct)
        else:
            return ''

    wedges, _, labels = ax.pie(values, autopct=formatter, **kwargs)
    return wedges


def donut(inside_values, inside_labels, outside_values, outside_labels,
          outside_groups, title=None):
    fig, ax = plt.subplots()

    if title is not None:
        ax.set_title(title)

    ax.axis('equal')

    width = 0.35
    colors_tab20c = list(plt.get_cmap('tab20c').colors)
    colors_set2 = list(plt.get_cmap('Set2').colors)
    colors_set3 = list(plt.get_cmap('Set3').colors)
    colors_pastel1 = list(plt.get_cmap('Pastel1').colors)

    # swap green and red
    # for i in range(4):
    #    tmp = colors[4 + i]
    #    colors[4 + i] = colors[8 + i]
    #    colors[8 + i] = tmp

    colors = []
    colors.extend(colors_tab20c[8:12])
    colors.append(colors_set2[5])
    colors.append(colors_set3[11])
    colors.append(colors_set3[1])
    colors.append(colors_pastel1[5])
    colors.extend(colors_tab20c[4:8])

    inside_colors = [colors[x * 4] for x in range(len(inside_values))]

    group_count = Counter(outside_groups)
    outside_colors = [colors[(i * 4) + ((j % 3) + 1)]
                      for i in list(set(outside_groups))
                      for j in range(group_count[i])]

    outside = pie(ax, outside_values, radius=1, pctdistance=1 - width / 2,
                  colors=outside_colors, startangle=90, counterclock=False,
                  textprops={'color': 'w', 'weight': 'bold',
                             'path_effects': [
                                 PathEffects.withStroke(linewidth=3,
                                                        foreground='black')]})
    inside = pie(ax, inside_values, radius=1 - width,
                 pctdistance=1 - (width / 2) / (1 - width),
                 colors=inside_colors, startangle=90, counterclock=False,
                 textprops={'color': 'w', 'weight': 'bold',
                            'path_effects': [PathEffects.withStroke(linewidth=3,
                                                                    foreground='black')]})
    plt.setp(inside + outside, width=width, edgecolor='white')

    wedges = []
    labels = []
    so_far = 0
    for i in list(set(outside_groups)):
        wedges.append(inside[i])
        labels.append(inside_labels[i])
        for j in range(group_count[i]):
            wedges.append(outside[so_far])
            labels.append(outside_labels[so_far])
            so_far += 1

    ax.legend(wedges, labels, frameon=True)
    plt.tight_layout()
    ludwig.contrib.contrib_command("visualize_figure", plt.gcf())
    plt.savefig(title+'.png')
    plt.show()


def confidence_fitlering_plot(thresholds, accuracies, dataset_kepts,
                              algorithm_names=None, title=None):
    assert len(accuracies) == len(dataset_kepts)
    num_algorithms = len(accuracies)

    sns.set_style('whitegrid')

    if num_algorithms == 1:
        colors = plt.get_cmap('tab10').colors
    else:  # num_algorithms > 1
        colors = plt.get_cmap('tab20').colors

    y_ticks_minor = np.linspace(0.0, 1.0, num=21)
    y_ticks_major = np.linspace(0.0, 1.0, num=11)
    y_ticks_major_labels = ['{:3.0f}%'.format(y * 100) for y in y_ticks_major]

    fig, ax1 = plt.subplots()

    if title is not None:
        ax1.set_title(title)

    ax1.grid(which='both')
    ax1.grid(which='minor', alpha=0.5)
    ax1.grid(which='major', alpha=0.75)
    ax1.set_xticks([x for idx, x in enumerate(thresholds) if idx % 2 == 0])
    ax1.set_xticks(thresholds, minor=True)

    ax1.set_xlim(-0.05, 1.05)
    ax1.set_xlabel('confidence threshold')

    ax1.set_ylim(0, 1.05)
    ax1.set_yticks(y_ticks_major)
    ax1.set_yticklabels(y_ticks_major_labels)
    ax1.set_yticks(y_ticks_minor, minor=True)

    ax2 = ax1.twinx()

    ax2.set_ylim(0, 1.05)
    ax2.set_yticks(y_ticks_major)
    ax2.set_yticklabels(y_ticks_major_labels)
    ax2.set_yticks(y_ticks_minor, minor=True)

    for i in range(len(accuracies)):
        algorithm_name = algorithm_names[
                             i] + ' ' if algorithm_names is not None and i < len(
            algorithm_names) else ''
        ax1.plot(thresholds, accuracies[i],
                 label='{} accuracy'.format(algorithm_name),
                 color=colors[i * 2],
                 linewidth=3)
        ax1.plot(thresholds, dataset_kepts[i],
                 label='{} data coverage'.format(algorithm_name),
                 color=colors[i * 2 + 1], linewidth=3)

    ax1.legend(frameon=True, loc=3)
    plt.tight_layout()
    ludwig.contrib.contrib_command("visualize_figure", plt.gcf())
    plt.savefig(title+'.png')
    plt.show()


def confidence_fitlering_data_vs_acc_plot(accuracies, dataset_kepts,
                                          model_names=None,
                                          dotted=False,
                                          decimal_digits=0,
                                          y_label='accuracy',
                                          title=None):
    assert len(accuracies) == len(dataset_kepts)

    sns.set_style('whitegrid')

    colors = plt.get_cmap('tab10').colors

    max_dataset_kept = max(
        [max(dataset_kept) for dataset_kept in dataset_kepts])

    x_ticks_minor = np.linspace(0.0, max_dataset_kept, num=21)
    x_ticks_major = np.linspace(0.0, max_dataset_kept, num=11)
    x_ticks_major_labels = [
        '{value:3.{decimal_digits}f}%'.format(
            decimal_digits=decimal_digits,
            value=x * 100
        ) for x in x_ticks_major
    ]
    y_ticks_minor = np.linspace(0.0, 1.0, num=21)
    y_ticks_major = np.linspace(0.0, 1.0, num=11)

    fig, ax = plt.subplots()

    if title is not None:
        ax.set_title(title)

    ax.grid(which='both')
    ax.grid(which='minor', alpha=0.5)
    ax.grid(which='major', alpha=0.75)
    ax.set_xticks(x_ticks_major)
    ax.set_xticks(x_ticks_minor, minor=True)
    ax.set_xticklabels(x_ticks_major_labels)
    ax.set_xlim(0, max_dataset_kept)
    ax.set_xlabel('data coverage')

    ax.set_ylim(0, 1)
    ax.set_yticks(y_ticks_major)
    ax.set_yticks(y_ticks_minor, minor=True)
    ax.set_ylabel(y_label)

    for i in range(len(accuracies)):
        curr_dotted = dotted[i] if isinstance(dotted,
                                              (list, tuple)) and i < len(
            dotted) else dotted
        algorithm_name = model_names[
                             i] + ' ' if model_names is not None and i < len(
            model_names) else ''
        ax.plot(dataset_kepts[i], accuracies[i], label=algorithm_name,
                color=colors[i],
                linewidth=3, linestyle=':' if curr_dotted else '-')

    ax.legend(frameon=True, loc=3)
    plt.tight_layout()
    ludwig.contrib.contrib_command("visualize_figure", plt.gcf())
    plt.savefig(title+'.png')
    plt.show()


def confidence_fitlering_data_vs_acc_multiline_plot(accuracies, dataset_kepts,
                                                    models_names,
                                                    title=None):
    assert len(accuracies) == len(dataset_kepts)

    sns.set_style('whitegrid')

    colors = plt.get_cmap('tab20').colors

    max_dataset_kept = max(
        [max(dataset_kept) for dataset_kept in dataset_kepts])

    x_ticks_minor = np.linspace(0.0, max_dataset_kept, num=21)
    x_ticks_major = np.linspace(0.0, max_dataset_kept, num=11)
    x_ticks_major_labels = ['{:3.0f}%'.format(x * 100) for x in x_ticks_major]
    y_ticks_minor = np.linspace(0.0, 1.0, num=21)
    y_ticks_major = np.linspace(0.0, 1.0, num=11)

    fig, ax = plt.subplots()

    if title is not None:
        ax.set_title(title)

    ax.grid(which='both')
    ax.grid(which='minor', alpha=0.5)
    ax.grid(which='major', alpha=0.75)
    ax.set_xticks(x_ticks_major)
    ax.set_xticks(x_ticks_minor, minor=True)
    ax.set_xticklabels(x_ticks_major_labels)
    ax.set_xlim(0, max_dataset_kept)
    ax.set_xlabel('data coverage')

    ax.set_ylim(0, 1)
    ax.set_yticks(y_ticks_major)
    ax.set_yticks(y_ticks_minor, minor=True)
    ax.set_ylabel('accuracy')

    for i in range(len(accuracies)):
        ax.plot(dataset_kepts[i], accuracies[i], color=colors[0],
                linewidth=1.0, alpha=0.35)

    legend_elements = [Line2D([0], [0], linewidth=1.0, color=colors[0])]
    ax.legend(legend_elements, models_names)
    plt.tight_layout()
    ludwig.contrib.contrib_command("visualize_figure", plt.gcf())
    plt.savefig(title+'.png')
    plt.show()


def confidence_fitlering_3d_plot(thresholds_1, thresholds_2, accuracies,
                                 dataset_kepts, threshold_fields=None,
                                 title=None):
    assert len(accuracies) == len(dataset_kepts)
    assert len(thresholds_1) == len(thresholds_2)

    thresholds_1, thresholds_2 = np.meshgrid(thresholds_1, thresholds_2)

    colors = plt.get_cmap('tab10').colors
    sns.set_style('white')

    z_ticks_minor = np.linspace(0.0, 1.0, num=21)
    z_ticks_major = np.linspace(0.0, 1.0, num=11)
    z_ticks_major_labels = ['{:3.0f}%'.format(z * 100) for z in z_ticks_major]

    fig = plt.figure()
    ax = Axes3D
    ax = fig.add_subplot(111, projection='3d')

    if title is not None:
        ax.set_title(title)

    ax.grid(which='both')
    ax.grid(which='minor', alpha=0.5)
    ax.grid(which='major', alpha=0.75)

    ax.set_xlabel('{} probability'.format(threshold_fields[0]))
    ax.set_ylabel('{} probability'.format(threshold_fields[1]))

    ax.set_xlim(np.min(thresholds_1), np.max(thresholds_1))
    ax.set_ylim(np.min(thresholds_2), np.max(thresholds_2))
    ax.set_zlim(0, 1)
    ax.set_zticks(z_ticks_major)
    ax.set_zticklabels(z_ticks_major_labels)
    ax.set_zticks(z_ticks_minor, minor=True)

    # ORRIBLE HACK, IT'S THE ONLY WAY TO REMOVE PADDING
    from mpl_toolkits.mplot3d.axis3d import Axis
    if not hasattr(Axis, '_get_coord_info_old'):
        def _get_coord_info_new(self, renderer):
            mins, maxs, centers, deltas, tc, highs = self._get_coord_info_old(
                renderer)
            mins += deltas / 4
            maxs -= deltas / 4
            return mins, maxs, centers, deltas, tc, highs

        Axis._get_coord_info_old = Axis._get_coord_info
        Axis._get_coord_info = _get_coord_info_new
    # END OF HORRIBLE HACK

    surf_1 = ax.plot_surface(thresholds_1, thresholds_2, accuracies,
                             alpha=0.5,
                             label='accuracy',
                             cmap=plt.get_cmap('winter'),
                             edgecolor='none')
    surf_2 = ax.plot_surface(thresholds_1, thresholds_2, dataset_kepts,
                             alpha=0.5,
                             label='data coverage',
                             cmap=plt.get_cmap('autumn'),
                             edgecolor='none')

    handle_1 = copy.copy(surf_1)
    handle_2 = copy.copy(surf_2)

    handle_1.set_color(colors[0])
    handle_2.set_color(colors[1])

    handle_1._edgecolors2d = handle_1._edgecolors3d
    handle_2._edgecolors2d = handle_2._edgecolors3d

    handle_1._facecolors2d = handle_1._facecolors3d
    handle_2._facecolors2d = handle_2._facecolors3d

    ax.legend(frameon=True, loc=3, handles=[handle_1, handle_2])

    plt.tight_layout()
    ludwig.contrib.contrib_command("visualize_figure", plt.gcf())
    plt.savefig(title+'.png')
    plt.show()


def threshold_vs_metric_plot(thresholds, scores, algorithm_names=None,
                             title=None):
    sns.set_style('whitegrid')

    colors = plt.get_cmap('tab10').colors

    # y_ticks_minor = np.linspace(0.0, 1.0, num=21)
    # y_ticks_major = np.linspace(0.0, 1.0, num=11)
    # y_ticks_major_labels = ['{:3.0f}%'.format(y * 100) for y in y_ticks_major]

    fig, ax1 = plt.subplots()

    if title is not None:
        ax1.set_title(title)

    ax1.grid(which='both')
    ax1.grid(which='minor', alpha=0.5)
    ax1.grid(which='major', alpha=0.75)
    ax1.set_xticks([x for idx, x in enumerate(thresholds) if idx % 2 == 0])
    ax1.set_xticks(thresholds, minor=True)

    # ax1.set_xlim(0, 1)
    ax1.set_xlabel('confidence threshold')

    # ax1.set_ylim(0, 1)
    # ax1.set_yticks(y_ticks_major)
    # ax1.set_yticklabels(y_ticks_major_labels)
    # ax1.set_yticks(y_ticks_minor, minor=True)

    for i in range(len(scores)):
        algorithm_name = algorithm_names[
                             i] + ' ' if algorithm_names is not None and i < len(
            algorithm_names) else ''
        ax1.plot(thresholds, scores[i], label=algorithm_name, color=colors[i],
                 linewidth=3, marker='o')

    ax1.legend(frameon=True)
    plt.tight_layout()
    ludwig.contrib.contrib_command("visualize_figure", plt.gcf())
    plt.savefig(title+'.png')
    plt.show()


def roc_curves(fpr_tprs, algorithm_names=None, title=None, graded_color=False):
    sns.set_style('whitegrid')

    colors = plt.get_cmap('tab10').colors
    colormap = plt.get_cmap('RdYlGn')

    y_ticks_minor = np.linspace(0.0, 1.0, num=21)
    y_ticks_major = np.linspace(0.0, 1.0, num=11)

    fig, ax = plt.subplots()

    if title is not None:
        ax.set_title(title)

    ax.grid(which='both')
    ax.grid(which='minor', alpha=0.5)
    ax.grid(which='major', alpha=0.75)

    ax.set_xlim(0, 1)
    ax.set_xlabel('False positive rate')

    ax.set_ylim(0, 1)
    ax.set_yticks(y_ticks_major)
    ax.set_yticks(y_ticks_minor, minor=True)
    ax.set_ylabel('True positive rate')

    plt.plot([0, 1], [0, 1], color='black', linewidth=3, linestyle='--')

    for i in range(len(fpr_tprs)):
        algorithm_name = algorithm_names[
                             i] + ' ' if algorithm_names is not None and i < len(
            algorithm_names) else ''
        color = colormap(i / len(fpr_tprs)) if graded_color else colors[i]
        ax.plot(fpr_tprs[i][0], fpr_tprs[i][1], label=algorithm_name,
                color=color,
                linewidth=3)

    ax.legend(frameon=True)
    plt.tight_layout()
    ludwig.contrib.contrib_command("visualize_figure", plt.gcf())
    plt.savefig(title+'.png')
    plt.show()


def calibration_plot(fraction_positives, mean_predicted_values,
                     algorithm_names=None):
    assert len(fraction_positives) == len(mean_predicted_values)

    sns.set_style('whitegrid')

    colors = plt.get_cmap('tab10').colors

    num_algorithms = len(fraction_positives)

    plt.figure(figsize=(9, 9))
    plt.grid(which='both')
    plt.grid(which='minor', alpha=0.5)
    plt.grid(which='major', alpha=0.75)

    plt.plot([0, 1], [0, 1], 'k:', label='Perfectly calibrated')

    for i in range(num_algorithms):
        # ax1.plot(mean_predicted_values[i], fraction_positives[i],
        #         label=algorithms[i] if algorithm_names is not None and i < len(algorithms) else '')

        # sns.tsplot(mean_predicted_values[i], fraction_positives[i], ax=ax1, color=colors[i])

        sns.regplot(mean_predicted_values[i], fraction_positives[i],
                    order=3, x_estimator=np.mean, color=colors[i], marker='o',
                    scatter_kws={'s': 40},
                    label=algorithm_names[
                        i] if algorithm_names is not None and i < len(
                        algorithm_names) else '')

    ticks = np.linspace(0.0, 1.0, num=11)
    plt.xlim([-0.05, 1.05])
    plt.xticks(ticks)
    plt.xlabel('Predicted probability')
    plt.ylabel('Observed probability')
    plt.ylim([-0.05, 1.05])
    plt.yticks(ticks)
    plt.legend(loc='lower right')
    plt.title('Calibration (reliability curve)')

    plt.tight_layout()
    ludwig.contrib.contrib_command("visualize_figure", plt.gcf())
    plt.savefig(title+'.png')
    plt.show()


def brier_plot(brier_scores, algorithm_names=None, title=None):
    sns.set_style('whitegrid')

    if title is not None:
        plt.title(title)

    colors = plt.get_cmap('tab10').colors

    plt.grid(which='both')
    plt.grid(which='minor', alpha=0.5)
    plt.grid(which='major', alpha=0.75)
    plt.xlabel('class')
    plt.ylabel('brier')

    x = np.array(range(brier_scores.shape[0]))
    for i in range(brier_scores.shape[1]):
        plt.plot(brier_scores[:, i],
                 label=algorithm_names[
                           i] + ' ' if algorithm_names is not None and i < len(
                     algorithm_names) else '',
                 color=colors[i], linewidth=3)

    plt.legend()
    plt.tight_layout()
    ludwig.contrib.contrib_command("visualize_figure", plt.gcf())
    plt.savefig(title+'.png')
    plt.show()


def predictions_distribution_plot(probabilities, algorithm_names=None):
    sns.set_style('whitegrid')

    colors = plt.get_cmap('tab10').colors

    num_algorithms = len(probabilities)

    plt.figure(figsize=(9, 9))
    plt.grid(which='both')
    plt.grid(which='minor', alpha=0.5)
    plt.grid(which='major', alpha=0.75)

    for i in range(num_algorithms):
        plt.hist(probabilities[i], range=(0, 1), bins=41, color=colors[i],
                 label=algorithm_names[
                     i] if algorithm_names is not None and i < len(
                     algorithm_names) else '',
                 histtype='stepfilled', alpha=0.5, lw=2)

    plt.xlabel('Mean predicted value')
    plt.xlim([0, 1])
    plt.xticks(np.linspace(0.0, 1.0, num=21))
    plt.ylabel('Count')
    plt.legend(loc='upper center', ncol=2)

    plt.tight_layout()
    ludwig.contrib.contrib_command("visualize_figure", plt.gcf())
    plt.savefig(title+'.png')
    plt.show()


def confusion_matrix_plot(confusion_matrix, labels=None, field=None):
    mpl.rcParams.update({'figure.autolayout': True})
    fig, ax = plt.subplots()

    ax.invert_yaxis()
    ax.xaxis.tick_top()
    ax.xaxis.set_label_position('top')

    cax = ax.matshow(confusion_matrix, cmap='viridis')

    ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
    ax.set_xticklabels([''] + labels, rotation=45, ha='left')
    ax.set_yticklabels([''] + labels)
    ax.grid(False)
    ax.tick_params(axis='both', which='both', length=0)
    fig.colorbar(cax, ax=ax, extend='max')
    ax.set_xlabel('Predicted {}'.format(field))
    ax.set_ylabel('Actual {}'.format(field))

    plt.tight_layout()
    ludwig.contrib.contrib_command("visualize_figure", plt.gcf())
    plt.savefig(title+'.png')
    plt.show()


def double_axis_line_plot(y1_sorted, y2, y1_name, y2_name, labels=None,
                          title=None):
    sns.set_style('whitegrid')

    colors = plt.get_cmap('tab10').colors

    fig, ax1 = plt.subplots()

    if title is not None:
        ax1.set_title(title)

    # ax1.grid(which='both')
    # ax1.grid(which='minor', alpha=0.5)
    # ax1.grid(which='major', alpha=0.75)

    ax1.set_xlabel('class (sorted by {})'.format(y1_name))
    ax1.set_xlim(0, len(y1_sorted) - 1)
    if labels is not None:
        ax1.set_xticklabels(labels, rotation=45, ha='right')
        ax1.set_xticks(np.arange(len(labels)))

    ax1.set_ylabel(y2_name, color=colors[1])
    ax1.tick_params('y', colors=colors[1])
    ax1.set_ylim(min(y2), max(y2))

    ax2 = ax1.twinx()
    ax2.set_ylabel(y1_name, color=colors[0])
    ax2.tick_params('y', colors=colors[0])
    ax2.set_ylim(min(y1_sorted), max(y1_sorted))

    ax1.plot(y2, label=y2_name, color=colors[1],
             linewidth=3)
    ax2.plot(y1_sorted, label=y1_name, color=colors[0],
             linewidth=4.0)

    fig.tight_layout()
    ludwig.contrib.contrib_command("visualize_figure", plt.gcf())
    plt.savefig(title+'.png')
    plt.show()


def plot_matrix(matrix, cmap='hot'):
    plt.matshow(matrix, cmap=cmap)
    ludwig.contrib.contrib_command("visualize_figure", plt.gcf())
    plt.savefig(title+'.png')
    plt.show()


def plot_distributions(distributions, labels=None, title=None):
    sns.set_style('whitegrid')

    colors = plt.get_cmap('tab10').colors

    fig, ax1 = plt.subplots()

    if title is not None:
        ax1.set_title(title)

    ax1.grid(which='both')
    ax1.grid(which='minor', alpha=0.5)
    ax1.grid(which='major', alpha=0.75)

    ax1.set_xlabel('class')

    ax1.set_ylabel('p')
    ax1.tick_params('y')

    for i, distribution in enumerate(distributions):
        ax1.plot(distribution, color=colors[i], alpha=0.6,
                 label=labels[i] if labels is not None and i < len(
                     labels) else 'Distribution {}'.format(i))

    ax1.legend(frameon=True)
    fig.tight_layout()
    ludwig.contrib.contrib_command("visualize_figure", plt.gcf())
    plt.savefig(title+'.png')
    plt.show()


def plot_distributions_difference(distribution, labels=None, title=None):
    sns.set_style('whitegrid')

    colors = plt.get_cmap('tab10').colors

    fig, ax1 = plt.subplots()

    if title is not None:
        ax1.set_title(title)

    ax1.grid(which='both')
    ax1.grid(which='minor', alpha=0.5)
    ax1.grid(which='major', alpha=0.75)

    ax1.set_xlabel('class')

    ax1.set_ylabel('p')
    ax1.tick_params('y')

    ax1.plot(distribution, color=colors[0])

    fig.tight_layout()
    ludwig.contrib.contrib_command("visualize_figure", plt.gcf())
    plt.savefig(title+'.png')
    plt.show()


def bar_plot(xs, ys, decimals=4, labels=None, title=None):
    assert len(xs) == len(ys)
    assert len(xs) > 0

    sns.set_style('whitegrid')

    fig, ax = plt.subplots()

    ax.grid(which='both')
    ax.grid(which='minor', alpha=0.5)
    ax.grid(which='major', alpha=0.75)

    if title is not None:
        ax.set_title(title)

    colors = plt.get_cmap('tab10').colors

    ax.invert_yaxis()  # labels read top-to-bottom

    maximum = ys.max()
    ticks = np.arange(len(xs))
    ax.set_yticks(ticks)
    if labels is None:
        ax.set_yticklabels(xs)
    else:
        ax.set_yticklabels(labels)

    ax.barh(ticks, ys, color=colors[0], align='center')

    for i, v in enumerate(ys):
        if v < maximum * (0.025 * decimals + 0.1):
            x = v + maximum * 0.01
            horizontal_alignment = 'left'
        else:
            x = v - maximum * 0.01
            horizontal_alignment = 'right'
        txt = ax.text(x, ticks[i], ('{:.' + str(decimals) + 'f}').format(v),
                      color='white',
                      fontweight='bold', verticalalignment='center',
                      horizontalalignment=horizontal_alignment)
        txt.set_path_effects(
            [PathEffects.withStroke(linewidth=3, foreground='black')])

    plt.tight_layout()
    ludwig.contrib.contrib_command("visualize_figure", plt.gcf())
    plt.savefig(title+'.png')
    plt.show()
