#MenuTitle: Print Selected Unicode
# encoding: utf-8
__doc__="""
Print the Unicode from selected glyphs.
"""

myGlyphs = Glyphs.font.glyphs
for number in myGlyphs:
	print number.unicode