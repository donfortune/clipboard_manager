import json
import sys
import clipboard

MAIN_DATA = 'clipboard.json'
#data = clipboard.paste()
#clipboard.copy('abc')
#print(data)
def save_items(filepath, data):
    with open(filepath, 'w') as file:
        json.dump(data, file)  #dump data to a json file

def read_saved_items(filepath):
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
            return data
    except:
         return {}

if len(sys.argv) == 2:
    entry = sys.argv[1]
    data = read_saved_items(MAIN_DATA)

    if entry == 'save':
        key = input('enter a key:')
        value = clipboard.paste()

        if key in data:
            data[key].append(value)
        else:
            data[key] = [value]
        save_items(MAIN_DATA, data)
        print('Data Saved')
    elif entry == 'load':
        key_to_load = input('enter a key to load:')
        if key_to_load in data:
            clipboard.copy(data[key_to_load])
            print('Data copied to clipboard.')
        else:
            print('key doesnt exist')
    elif entry == 'delete':
        key_to_delete = input('enter key to delete')
        if key_to_delete in data:
            del data[key_to_delete]
            save_items(MAIN_DATA, data)
            print('item deleted')

    elif entry == 'list':
        print(data)
    else:
        print('unknown command')
else:
    print('enter  your command')




