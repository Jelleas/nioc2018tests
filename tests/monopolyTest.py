import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as asserts

@t.test(0)
def throwAvg(test):
	def testMethod():
		throw = lib.getFunction("throw", test.fileName)
		n = 10000
		s = sum(throw() for i in range(n))
		return asserts.between(s / n, 6.5, 7.5)

	test.test = testMethod
	test.description = lambda : "throw() returns 7 on average"

@t.test(10)
def throwNums(test):
	def testMethod():
		throw = lib.getFunction("throw", test.fileName)
		return asserts.containsOnly([throw() for i in range(10000)], list(range(2,13)))

	test.test = testMethod
	test.description = lambda : "throw() returns only the numbers 2 to 12"

@t.test(20)
def throwEvenDist(test):
	def testMethod():
		throw = lib.getFunction("throw", test.fileName)
		throws = [throw() for i in range(100000)]
		dist = [0] * 13
		for t in throws:
			if 0 <= t < 13:
				dist[t] += 1
		return (dist[2] * 3) < dist[7] and dist[2] != 0

	test.test = testMethod
	test.description = lambda : "throw() returns some occurences (7) more than others (2)"

@t.test(30)
def correct(test):
	def testMethod():
		output = lib.outputOf(
			test.fileName,
			overwriteAttributes = [("__name__", "__main__")]
		)
		line = lib.getLine(output, 0)
		testResult = asserts.numberOnLine(147, line, deviation = 5)

		if not testResult and asserts.numberOnLine(147, output, deviation = 5):
			test.fail = lambda info : "hint: make sure the number of throws is on the first line of the output"

		return testResult

	test.test = testMethod
	test.description = lambda : "prints the correct number of throws to buy everything"