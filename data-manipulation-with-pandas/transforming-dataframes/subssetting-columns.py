# Select the individuals column
individuals = homelessness["individuals"]

# Select the state and family_members columns
state_fam = homelessness[["state", "family_members"]]

# Select only the individuals and state columns, in that order
ind_state = homelessness[["individuals", "state"]]