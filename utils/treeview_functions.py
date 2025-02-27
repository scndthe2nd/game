#treeview_functions.py
"""Module providing simplified treeview functions to tkinter"""

import tkinter as tk

# Function to add selected items to the list
def add_items(treeview, selected_list, update_function):
    """Add items to treeview list"""
    selected_items = treeview.selection()
    if not selected_items:
        return
    for item in selected_items:
        value = treeview.item(item, "values")
        if value not in selected_list:
            selected_list.append(value)
    update_function()

# Function to remove selected items from the list
def remove_items(treeview, selected_list, update_function):
    """Remove items from treeview list"""
    selected_items = treeview.selection()
    for item in selected_items:
        value = treeview.item(item, "values")
        if value in selected_list:
            selected_list.remove(value)
    update_function()

# Function to add all items to the selected list
def add_all_items(treeview, selected_list, update_function):
    """Add All items to treeview list"""
    for item in treeview.get_children():
        value = treeview.item(item, "values")
        if value not in selected_list:
            selected_list.append(value)
    update_function()

# Function to remove all items from the selected list
def remove_all_items(selected_list, update_function):
    """Remove All items from treeview list"""
    selected_list.clear()
    update_function()

# Function to update the treeview
def update_treeview(treeview, items):
    """Refresh Treeview List with Updated Values"""
    for item in treeview.get_children():
        treeview.delete(item)
    for value in items:
        treeview.insert("", tk.END, values=value)

# Function to sort treeview column
def sort_treeview_column(tree, col, reverse):
    """Sort Treeview List"""
    data = [(tree.set(child, col), child) for child in tree.get_children('')]
    data.sort(reverse=reverse)
    for index, child in enumerate(data):
        tree.move(child, '', index)
    tree.heading(col, command=lambda: sort_treeview_column(tree, col, not reverse))

# Move items up a list
def move_item_up(treeview):
    """Move Selected Item in treeview list Up"""
    selected_items = treeview.selection()
    if not selected_items:
        return
    for item in selected_items:
        prev_item = treeview.prev(item)
        if prev_item:
            treeview.move(item, treeview.parent(item), treeview.index(prev_item))

# ove items down a list
def move_item_down(treeview):
    """Move Selected Item in treeview list Down"""
    selected_items = treeview.selection()
    if not selected_items:
        return
    for item in reversed(selected_items):
        next_item = treeview.next(item)
        if next_item:
            treeview.move(item, treeview.parent(item), treeview.index(next_item) + 1)
# End-of-file (EOF)
