def name_in_list(srch_for, list):
    found = []
    for i in list:
        if i.name.find(srch_for) != -1:
            found.append(i)
    if len(found) == 0:
        return {"find_any": False, "more_spec": False, "found": found}
    elif len(found) == 1:
        return {"find_any": True, "more_spec": False, "found": found}
    else:
        return {"find_any": True, "more_spec": True, "found": found}

# to_get = cmd_input[1]
#             items_found = []
#             for i in player1.current_room.items:
#                 if i.name.find(to_get) != -1:
#                     items_found.append(i)
#             if len(items_found) == 0:
#                 print(f"You don't see a {to_get}.")
#                 continue
#             elif len(items_found) > 1:
#                 print(f"Please be more specific. You might mean:")
#                 for i in items_found:
#                     print(i.name)
#                 continue
#             else:
#                 items_found[0].on_take()
#                 player1.items.append(items_found[0])
#                 player1.current_room.items.remove(items_found[0])
#                 continue