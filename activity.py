import itertools

def flatten(sample_list):
    # iterate through the multidimentional list and return a one dimentional list
    return(list(itertools.chain(*sample_list)))

    # option 2 iterate the list
    # return([element for sub in sample_list for element in sub])


sample_list = []
choice = input("Show one-dimentional list: A) Use sample list. B) Enter sample list. [A/B]? : ").lower()
if choice == "a":
    sample_list = [['good','2','3'], ['4','better','6'], ['7','8','best']]
elif choice == "b":
    #define the number of sub list
    sub_list = int(input("Enter the number of sub list: "))
    #separate the list items per defined sub list
    sample_list = [(input("Enter the list items seperated by comma: ").split(",")) for _ in range(sub_list)]
else:
    print("Invalid choice")

if sample_list:
    print("\nSample list:", sample_list)
    print("\nOne dimentional list:", flatten(sample_list))