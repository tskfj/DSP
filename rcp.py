recipes = {
    # raw material
    'coal': (
        'coal',
        'NULL',
        'NULL',
        'NULL',
        'raw material',
        1, 0, 0, 0, 1),
    'copper_ore': (
        'copper_ore',
        'NULL',
        'NULL',
        'NULL',
        'raw material',
        1, 0, 0, 0, 1),
    'deuterium': (
        'deuterium',
        'NULL',
        'NULL',
        'NULL',
        'raw material',
        1, 0, 0, 0, 1),
    'fire_ice': (
        'fire_ice',
        'NULL',
        'NULL',
        'NULL',
        'raw material',
        1, 0, 0, 0, 1),
    'hydrogen': (
        'hydrogen',
        'NULL',
        'NULL',
        'NULL',
        'raw material',
        1, 0, 0, 0, 1),
    'iron_ore': (
        'iron_ore',
        'NULL',
        'NULL',
        'NULL',
        'raw material',
        1, 0, 0, 0, 1),
    'organic_crystal': (
        'organic_crystal',
        'NULL',
        'NULL',
        'NULL',
        'raw material',
        1, 0, 0, 0, 1),
    'silicon_ore': (
        'silicon_ore',
        'NULL',
        'NULL',
        'NULL',
        'raw material',
        1, 0, 0, 0, 1),
    'spiniform_stalagmite_crystal': (
        'spiniform_stalagmite_crystal',
        'NULL',
        'NULL',
        'NULL',
        'raw material',
        1, 0, 0, 0, 1),
    'stone': (
        'stone',
        'NULL',
        'NULL',
        'NULL',
        'raw material',
        1, 0, 0, 0, 1),
    'sulfuric_acid': (
        'sulfuric_acid',
        'NULL',
        'NULL',
        'NULL',
        'raw material',
        1, 0, 0, 0, 1),
    'titanium_ore': (
        'titanium_ore',
        'NULL',
        'NULL',
        'NULL',
        'raw material',
        1, 0, 0, 0, 1),
    'water': (
        'water',
        'NULL',
        'NULL',
        'NULL',
        'raw material',
        1, 0, 0, 0, 1),

    # parts
    'carbon_nanotube': (
        'carbon_nanotube',
        'spiniform_stalagmite_crystal',
        'NULL',
        'NULL',
        'parts',
        2, 2, 0, 0, 4),
    'casimir_crystal': (
        'casimir_crystal',
        'titanium_crystal',
        'graphene',
        'hydrogen',
        'parts',
        1, 1, 2, 12, 4),
    'circuit_board': (
        'circuit_board',
        'iron_ingot',
        'copper_ingot',
        'NULL',
        'parts',
        2, 2, 1, 0, 1),
    'copper_ingot': (
        'copper_ingot',
        'copper_ore',
        'NULL',
        'NULL',
        'parts',
        1, 1, 0, 0, 1),
    'deuteron_fuel_rod': (
        'deuteron_fuel_rod',
        'titanium_alloy',
        'deuterium',
        'super-magnetic_ring',
        'parts',
        2, 1, 20, 1, 12),
    'dyson_sphere_component': (
        'dyson_sphere_component',
        'frame_material',
        'solar_sail',
        'processor',
        'parts',
        1, 3, 3, 3, 8),
    'electric_motor': (
        'electric_motor',
        'iron_ingot',
        'gear',
        'magnetic_coil',
        'parts',
        1, 2, 1, 1, 2),
    'electromagnetic_turbine': (
        'electromagnetic_turbine',
        'electric_motor',
        'magnetic_coil',
        'NULL',
        'parts',
        1, 2, 2, 0, 2),
    'energetic_graphite': (
        'energetic_graphite',
        'coal',
        'NULL',
        'NULL',
        'parts',
        1, 2, 0, 0, 2),
    'frame_material': (
        'frame_material',
        'carbon_nanotube',
        'titanium_alloy',
        'high-purity_silicon',
        'parts',
        1, 4, 1, 1, 6),
    'gear': (
        'gear',
        'iron_ingot',
        'NULL',
        'NULL',
        'parts',
        1, 1, 0, 0, 1),
    'glass': (
        'glass',
        'stone',
        'NULL',
        'NULL',
        'parts',
        1, 2, 0, 0, 2),
    'graphene': (
        'graphene',
        'fire_ice',
        'NULL',
        'NULL',
        'parts',
        2, 2, 0, 0, 2),
    'high-purity_silicon': (
        'high-purity_silicon',
        'silicon_ore',
        'NULL',
        'NULL',
        'parts',
        1, 2, 0, 0, 2),
    'iron_ingot': (
        'iron_ingot',
        'iron_ore',
        'NULL',
        'NULL',
        'parts',
        1, 1, 0, 0, 1),
    'magnet': (
        'magnet',
        'iron_ore',
        'NULL',
        'NULL',
        'parts',
        1, 1, 0, 0, 1.5),
    'magnetic_coil': (
        'magnetic_coil',
        'magnet',
        'copper_ingot',
        'NULL',
        'parts',
        2, 2, 1, 0, 1),
    'microcrystalline_component': (
        'microcrystalline_component',
        'high-purity_silicon',
        'copper_ingot',
        'NULL',
        'parts',
        1, 2, 1, 0, 2),
    'photon_combiner': (
        'photon_combiner',
        'prism',
        'circuit_board',
        'NULL',
        'parts',
        1, 2, 1, 0, 3),
    'plane_filter': (
        'plane_filter',
        'casimir_crystal',
        'titanium_glass',
        'NULL',
        'parts',
        1, 1, 2, 0, 12),
    'prism': (
        'prism',
        'glass',
        'NULL',
        'NULL',
        'parts',
        2, 3, 0, 0, 2),
    'processor': (
        'processor',
        'circuit_board',
        'microcrystalline_component',
        'NULL',
        'parts',
        1, 2, 2, 0, 3),
    'quantum_chip': (
        'quantum_chip',
        'processor',
        'plane_filter',
        'NULL',
        'parts',
        1, 2, 2, 0, 6),
    'small_carrier_rocket': (
        'small_carrier_rocket', 
        'dyson_sphere_component', 
        'deuteron_fuel_rod', 
        'quantum_chip', 
        'parts',
        1, 2, 4, 2, 6),
    'solar_sail': (
        'solar_sail',
        'graphene',
        'photon_combiner',
        'NULL',
        'parts',
        2, 1, 1, 0, 4),
    'steel': (
        'steel',
        'iron_ingot',
        'NULL',
        'NULL',
        'parts',
        1, 3, 0, 0, 3),
    'super-magnetic_ring': (
        'super-magnetic_ring',
        'electromagnetic_turbine',
        'magnet',
        'energetic_graphite',
        'parts',
        1, 2, 3, 1, 3),
    'titanium_alloy': (
        'titanium_alloy',
        'titanium_ingot',
        'steel',
        'sulfuric_acid',
        'parts',
        4, 4, 4, 8, 12),
    'titanium_crystal': (
        'titanium_crystal',
        'organic_crystal',
        'titanium_ingot',
        'NULL',
        'parts',
        1, 1, 3, 0, 4),
    'titanium_glass': (
        'titanium_glass',
        'glass',
        'titanium_ingot',
        'water',
        'parts',
        2, 2, 2, 2, 5),
    'titanium_ingot': (
        'titanium_ingot',
        'titanium_ore',
        'NULL',
        'NULL',
        'parts',
        1, 2, 0, 0, 2),
}

#   item name: (
#       output,
#       input1,
#       input2,
#       input3,
#       type,
#       output_rate, input1_rate, input2_rate, input3_rate, lead_time),
