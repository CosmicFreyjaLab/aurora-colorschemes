# Refactored Cosmic Sans generator with fontTools - All fixes applied

from fontTools.ttLib import TTFont, newTable
from fontTools.pens.ttGlyphPen import TTGlyphPen

font = TTFont()

# Create required tables
font.setGlyphOrder(['.notdef', 'A', 'infinity'])
head = newTable('head')
head.unitsPerEm = 1000
head.flags = 0  # Required for maxp table recalculation
font['head'] = head
font['hhea'] = newTable('hhea')
font['maxp'] = newTable('maxp')
font['name'] = newTable('name')
font['OS/2'] = newTable('OS/2')
font['cmap'] = newTable('cmap')
font['glyf'] = newTable('glyf')
font['hmtx'] = newTable('hmtx')

# Initialize maxp table version
font['maxp'].tableVersion = 0x00005000

# Prepare glyphs
glyphs = {}
pen_notdef = TTGlyphPen(None)
glyphs['.notdef'] = pen_notdef.glyph()

# Add glyph 'A'
pen_A = TTGlyphPen(None)
pen_A.moveTo((100, 0))
pen_A.lineTo((300, 700))
pen_A.lineTo((500, 0))
pen_A.closePath()
pen_A.moveTo((200, 250))
pen_A.lineTo((400, 250))
pen_A.closePath()
glyphs['A'] = pen_A.glyph()

# Add glyph 'infinity'
pen_inf = TTGlyphPen(None)
pen_inf.moveTo((100, 300))
pen_inf.curveTo((100, 100), (500, 100), (500, 300))
pen_inf.curveTo((500, 500), (100, 500), (100, 300))
pen_inf.closePath()
glyphs['infinity'] = pen_inf.glyph()

# Assign glyphs to 'glyf'
font['glyf'].glyphs = glyphs

# Assign hmtx metrics properly
font['hmtx'].metrics = {name: (600, 0) for name in font.getGlyphOrder()}

# Save the font
font.save('CosmicSans.ttf')
print("Cosmic Sans generated with fontTools!")

# Test cases
if __name__ == "__main__":
    try:
        loaded_font = TTFont('CosmicSans.ttf')
        print("Test Passed: CosmicSans.ttf successfully created and loaded.")
    except Exception as e:
        print("Test Failed:", e)

    # Validate glyphs presence
    try:
        for glyph_name in ['.notdef', 'A', 'infinity']:
            assert glyph_name in loaded_font.getGlyphOrder(), f"Glyph {glyph_name} missing"
        print("Additional Test Passed: Glyphs '.notdef', 'A', and 'infinity' exist.")
    except AssertionError as e:
        print("Additional Test Failed:", e)

    # Check hmtx metrics exist
    try:
        for glyph_name in ['.notdef', 'A', 'infinity']:
            width, lsb = loaded_font['hmtx'].metrics[glyph_name]
            assert width == 600, f"Width for {glyph_name} is incorrect"
        print("HMTX Test Passed: Metrics for glyphs are correctly set.")
    except Exception as e:
        print("HMTX Test Failed:", e)

