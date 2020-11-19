from skyline_horizontal_brushstrokes.skyline_horizontal_brushstrokes import count_skyline_horizontal_brushstrokes

def test_count_strokes_empty_array():
    assert count_skyline_horizontal_brushstrokes([]) == 0;

def test_count_strokes_one_building():
    building_height = 5;
    assert count_skyline_horizontal_brushstrokes([building_height]) == building_height;

def test_count_strokes_two_buidings_together():
    building1_height = 5;
    building2_height = 8;
    assert count_skyline_horizontal_brushstrokes([building1_height, building2_height]) == max(building1_height, building2_height);

def test_count_strokes_same_height_buildings():
    assert count_skyline_horizontal_brushstrokes([1,1,1,1]) == 1;

def test_count_strokes_different_height_buildings():
    assert count_skyline_horizontal_brushstrokes([1,3,2,1,2,1,5,3,3,4,2]) == 9;

def test_count_strokes_too_tall_buildings():
    assert count_skyline_horizontal_brushstrokes([20000000000,3000000000]) == -1;








