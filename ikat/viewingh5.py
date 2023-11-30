import h5py

# Open the .h5 file
with h5py.File('ikat_backend\ikat\my_model.h5', 'r') as f:
    # List all groups and datasets within the file
    def print_attrs(name, obj):
        print(name)
        for key, val in obj.attrs.items():
            print(f"    {key}: {val}")
    f.visititems(print_attrs)
