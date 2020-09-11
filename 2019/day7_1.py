image_width = 25
image_height = 6

def read_in_chunks(file_object, chunk_size=image_width):
    """Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1k."""
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data

def count_instances_in_layer(layer, digit):
    sum = 0
    for row in layer:
        sum += row.count(digit)
    return sum


f = open('input/day7.txt')
rows = [chunk for chunk in read_in_chunks(f)]
image_data = list(zip(*(iter(rows),) * image_height))
occurrences_list = [count_instances_in_layer(layer, '0') for layer in image_data]
layer_number_of_interest = occurrences_list.index(min(occurrences_list))
layer_of_interest = image_data[layer_number_of_interest]
print(count_instances_in_layer(layer_of_interest, '1') * count_instances_in_layer(layer_of_interest, '2'))
