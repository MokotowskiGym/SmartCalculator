p = {"r":162, "g":32, "b":255}
lb = {"r":80, "g":208, "b":255}
y = {"r":255, "g":224, "b":32}

colors = {"Purple":p,"Light Blue":lb,"Yellow":y}

# colors.update("red":5)
values =  [*colors["Purple"].values()]
print (tuple(values))
