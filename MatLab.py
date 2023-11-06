#!/usr/bin/env python
#Title: SbicolorProject - Align Sequences
#Graduate Student: Joel Shin
#PI: Dr. Yim

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.path import Path

#RING-C2	N-Cys-(2)-Cys-(13)-Cys-(1)-Cys-(4)-Cys-(2)-Cys-(10, 16)-Cys-(2)-Cys-C

verts = [(0,6), (2, 6), (2,4), (2,0), (6,-4), (10,0), (10,4), (6,0), (6,4), (10,8), (14,4), (14,0), (14,-2), (16,-2)]

#verts = [N-Terminus, Connect Curve, Cys1, Cys2, Connect Curve, Cys3, Cys4, Cys5, Cys6, Connect Curve, Cys7, Cys8, Connect Curve, C-Terminus]

codes = [Path.MOVETO, Path.CURVE3, Path.LINETO, Path.LINETO, Path.CURVE3, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.CURVE3, Path.LINETO, Path.LINETO, Path.CURVE3, Path.LINETO]

path = Path(verts, codes)

fig, ax = plt.subplots(figsize=(20, 13))

#fig, ax = plt.subplots()
patch = patches.PathPatch(path, facecolor = 'none', lw = 2)
ax.add_patch(patch)

r = 0.7

n_terminus = patches.Circle((0, 6), r, fill=True, color='yellow')
ax.add_patch(n_terminus)
first_ligand = patches.Circle((2, 4), r, fill=True, color='lightblue')
ax.add_patch(first_ligand)
second_ligand = patches.Circle((2, 0), r, fill=True, color='lightblue')
ax.add_patch(second_ligand)
third_ligand = patches.Circle((10, 0), r, fill=True, color='lightblue')
ax.add_patch(third_ligand)
fourth_ligand = patches.Circle((10, 4), r, fill=True, color='lightgreen')
ax.add_patch(fourth_ligand)
fifth_ligand = patches.Circle((6, 0), r, fill=True, color='pink')
ax.add_patch(fifth_ligand)
sixth_ligand = patches.Circle((6, 4), r, fill=True, color='lightblue')
ax.add_patch(sixth_ligand)
seventh_ligand = patches.Circle((14, 4), r, fill=True, color='lightblue')
ax.add_patch(seventh_ligand)
eigth_cys = patches.Circle((14, 0), r, fill=True, color='lightblue')
ax.add_patch(eigth_cys)
c_terminus = patches.Circle((16, -2), r, fill=True, color='yellow')
ax.add_patch(c_terminus)

# Metal
x_cys_1to5 = [2 + r, 6 - r]
y_cys_1to5 = [4 - r, 0 + r]
x_cys_2to6 = [2 + r, 6 - r]
y_cys_2to6 = [0 + r, 4 - r]
x_cys_4to8 = [10 + r, 14 - r]
y_cys_4to8 = [4 - r, 0 + r]
x_cys_3to7 = [10 + r, 14 - r]
y_cys_3to7 = [0 + r, 4 - r]

ax.plot(x_cys_1to5, y_cys_1to5, color = 'orange', linestyle='--', linewidth=5)
ax.plot(x_cys_2to6, y_cys_2to6, color = 'orange', linestyle='--', linewidth=5)
ax.plot(x_cys_4to8, y_cys_4to8, color = 'orange', linestyle='--', linewidth=5)
ax.plot(x_cys_3to7, y_cys_3to7, color = 'orange', linestyle='--', linewidth=5)

# Metal
first_metal = patches.Circle((4, 2), r, fill=True, color='orange')
ax.add_patch(first_metal)
second_metal = patches.Circle((12, 2), r, fill=True, color='orange')
ax.add_patch(second_metal)

ax.text(0, 6, 'N', color='black', ha='center', va='center', fontsize=40, weight='bold')    #N-Terminus with circle inside
ax.text(2, 4, 'Cys', color='black', ha='center', va='center', fontsize=40, weight='bold')  #Cys1
ax.text(2, 0, 'Cys', color='black', ha='center', va='center', fontsize=40, weight='bold')  #Cys2
ax.text(10, 0, 'Cys', color='black', ha='center', va='center', fontsize=40, weight='bold')  #Cys3
ax.text(10, 4, 'His', color='black', ha='center', va='center', fontsize=40, weight='bold')  #Cys
ax.text(6, 0, 'Ser', color='black', ha='center', va='center', fontsize=40, weight='bold')  #Cys4
ax.text(6, 4, 'Cys', color='black', ha='center', va='center', fontsize=40, weight='bold')  #Cys5
ax.text(14, 4, 'Cys', color='black', ha='center', va='center', fontsize=40, weight='bold')  #Cys6
ax.text(14, 0, 'Cys', color='black', ha='center', va='center', fontsize=40, weight='bold')  #Cys7
ax.text(16, -2, 'C', color='black', ha='center', va='center', fontsize=40, weight='bold')    #N-Terminus with circle inside

# Metal
ax.text(4, 2, r'$\mathbf{Zn}^\mathbf{+2}$', color='black', ha='center', va='center', fontsize=35, weight='bold')
ax.text(12, 2, r'$\mathbf{Zn}^\mathbf{+2}$', color='black', ha='center', va='center', fontsize=35, weight='bold')

# Amino Acid Between
ax.text(1.5, 2, r'$\mathbf{X}_\mathbf{2}$', color='black', ha='center', va='center', fontsize=40, weight='bold')  #Cys1-Cys2
ax.text(5.7, -2.5, r'$\mathbf{X}_\mathbf{14}$', color='black', ha='center', va='center', fontsize=40, weight='bold')    #Cys2-Cys3
ax.text(9.1, 2, r'$\mathbf{X}_\mathbf{4}$', color='black', ha='center', va='center', fontsize=40, weight='bold')  #Cys3-Cys4
ax.text(7.9, 3, r'$\mathbf{X}_\mathbf{3}$', color='black', ha='center', va='center', fontsize=40, weight='bold')  #Cys4-Cys5
ax.text(6.5, 2, r'$\mathbf{X}_\mathbf{2}$', color='black', ha='center', va='center', fontsize=40, weight='bold')  #Cys6-Cys7
ax.text(10, 6.5, r'$\mathbf{X}_\mathbf{14 - 18}$', color='black', ha='center', va='center', fontsize=40, weight='bold') #Cys7-Cys8
ax.text(15, 2, r'$\mathbf{X}_\mathbf{2}$', color='black', ha='center', va='center', fontsize=40, weight='bold')

# Formula
#ax.text(8, -4, 'RING-C2 N-Cys-(2)-Cys-(13)-Cys-(1)-Cys-(4)-Cys-(2)-Cys-(10, 16)-Cys-(2)-Cys-C', color='black', ha='center', va='center', fontsize=10)

ax.set_xlim(0 - r, 16 + r)
ax.set_ylim(-2.5 - r, 6.5 + r)

# Hide the x-axis and y-axis
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_color('none')
ax.spines['left'].set_color('none')
ax.spines['right'].set_color('none')
ax.tick_params(axis='both', which='both', length=0)

# Hide the numbers (ticks) on both the x-axis and y-axis
ax.set_xticks([])
ax.set_yticks([])

plt.show()
