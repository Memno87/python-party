formatter = "%r %r %r %r %r"

print formatter % (1, 2, 3, 4, 5)
print formatter % ("one", "two", "three", "four", "amazing")
print formatter % (True, False, False, True, True)
print formatter % (formatter, formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing right",
	"That you could've type up right.",
	"But it didn't sing.",
	"So I said goodnight.",
	"Another test."
	)

