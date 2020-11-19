def count_skyline_horizontal_brushstrokes(input_array):
    count_strokes = 0;
    last_height = 0;
    for building_height in input_array:
        if building_height >= last_height:
            count_strokes = count_strokes + (building_height - last_height);
        last_height = building_height
        if count_strokes > 1000000000:
            return -1;
    return count_strokes;
