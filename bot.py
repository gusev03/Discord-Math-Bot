import hikari
import lightbulb
import math
import statistics as stats

bot = lightbulb.BotApp(
    token = , # REDACTED
    default_enabled_guilds = ()   # REDACTED
    )

# Converts float to int if possible
def int_check(val):
    if val.is_integer():
        val = int(val)
    return val

# /add [num1 = float] [num2 = float]
@bot.command
@lightbulb.option('num2', 'second number', type=float)
@lightbulb.option('num1', 'first number', type=float)
@lightbulb.command('add', 'Adds two numbers')
@lightbulb.implements(lightbulb.SlashCommand)
async def add(context):
    num1 = context.options.num1
    num2 = context.options.num2
    val = num1 + num2
    val = int_check(val)
    await context.respond(val)

# /sub [num1 = float] [num2 = float]
@bot.command
@lightbulb.option('num2', 'second number', type=float)
@lightbulb.option('num1', 'first number', type=float)
@lightbulb.command('sub', 'Subtracts two numbers')
@lightbulb.implements(lightbulb.SlashCommand)
async def sub(context):
    num1 = context.options.num1
    num2 = context.options.num2
    val = num1 - num2
    val = int_check(val)
    await context.respond(val)

# /mul [num1 = float] [num2 = float]
@bot.command
@lightbulb.option('num2', 'second number', type=float)
@lightbulb.option('num1', 'first number', type=float)
@lightbulb.command('mul', 'Multiplies two numbers')
@lightbulb.implements(lightbulb.SlashCommand)
async def mul(context):
    num1 = context.options.num1
    num2 = context.options.num2
    val = num1 * num2
    val = int_check(val)
    await context.respond(val)


# /div [num1 = float] [num2 = float]
@bot.command
@lightbulb.option('num2', 'second number', type=float)
@lightbulb.option('num1', 'first number', type=float)
@lightbulb.command('div', 'Divides two numbers')
@lightbulb.implements(lightbulb.SlashCommand)
async def div(context):
    num1 = context.options.num1
    num2 = context.options.num2
    if num2 == 0:
        await context.respond("You can't divide by 0!")
        return
    val = num1 / num2
    val = int_check(val)
    await context.respond(val)

# /floordiv [num1 = float] [num2 = float]
@bot.command
@lightbulb.option('num2', 'second number', type=float)
@lightbulb.option('num1', 'first number', type=float)
@lightbulb.command('floordiv', 'Floor divides two numbers')
@lightbulb.implements(lightbulb.SlashCommand)
async def floordiv(context):
    num1 = context.options.num1
    num2 = context.options.num2
    if num2 == 0:
        await context.respond("You can't divide by 0!")
        return
    val = num1 // num2
    val = int_check(val)
    await context.respond(val)

# /mod [num1 = float] [num2 = float]
@bot.command
@lightbulb.option('num2', 'second number', type=float)
@lightbulb.option('num1', 'first number', type=float)
@lightbulb.command('mod', 'Finds remainder when dividing two numbers')
@lightbulb.implements(lightbulb.SlashCommand)
async def mod(context):
    num1 = context.options.num1
    num2 = context.options.num2
    if num2 == 0:
        await context.respond("You can't divide by 0!")
        return
    val = num1 % num2
    val = int_check(val)
    await context.respond(val)

# /sqrt [num = float]
@bot.command
@lightbulb.option('num', 'number', type=float)
@lightbulb.command('sqrt', 'Computes the square root of a number')
@lightbulb.implements(lightbulb.SlashCommand)
async def sqrt(context):
    num = context.options.num
    if num < 0:
        val = math.sqrt(-num)
        val = int_check(val)
        val = str(val) + 'i'
    else:
        val = math.sqrt(num)
        val = int_check(val)
    await context.respond(val)

# /pow [base = float] [exponent = float]
@bot.command
@lightbulb.option('exponent', 'exponent', type=float)
@lightbulb.option('base', 'base', type=float)
@lightbulb.command('pow', 'Computes the "base" raised to the "exponent" power')
@lightbulb.implements(lightbulb.SlashCommand)
async def pow(context):
    base = context.options.base
    exponent = context.options.exponent
    if base and (1 / exponent) == (1 // exponent) and (1 // exponent) % 2 == 0:
        val = math.pow(-base, exponent)
        val = int_check(val)
        val = str(val) + 'i'
    else:
        val = math.pow(base, exponent)
        val = int_check(val)
    await context.respond(val)

# /factorial [num = int]
@bot.command
@lightbulb.option('num', 'number', type=int)
@lightbulb.command('factorial', 'Computes the factorial of nonnegative integers')
@lightbulb.implements(lightbulb.SlashCommand)
async def factorial(context):
    num = context.options.num
    if num < 0:
        await context.respond("You can't compute the factorial of a negative number!")
    else:
        await context.respond(math.factorial(num))

# /exp [num = float]
@bot.command
@lightbulb.option('num', 'number', type=float)
@lightbulb.command('exp', 'Computes e to the power of the number')
@lightbulb.implements(lightbulb.SlashCommand)
async def exp(context):
    num = context.options.num
    val = math.exp(num)
    val = int_check(val)
    await context.respond(val)

# /ln [num = float]
@bot.command
@lightbulb.option('num', 'number', type=float)
@lightbulb.command('ln', 'Computes a base e logarithm of a number')
@lightbulb.implements(lightbulb.SlashCommand)
async def ln(context):
    num = context.options.num
    if num <= 0:
        await context.respond("You can't compute the logarithm of a nonpositive number!")
    else:
        val = math.log(num)
        val = int_check(val)
        await context.respond(val)

# /log [base = float] [num = float]
@bot.command
@lightbulb.option('num', 'number', type=float)
@lightbulb.option('base', 'base value', type=float)
@lightbulb.command('log', 'Computes a positive base logarithm of a number')
@lightbulb.implements(lightbulb.SlashCommand)
async def log(context):
    base = context.options.base
    num = context.options.num
    if num <= 0:
        await context.respond("You can't compute the logarithm of a nonpositive number!")
    if base <= 0:
        await context.respond("The base value needs to be positive!")
    else:
        await context.respond(math.log(num, base))

# /log10 [num = float]
@bot.command
@lightbulb.option('num', 'number', type=float)
@lightbulb.command('log10', 'Computes a base 10 logarithm of a number')
@lightbulb.implements(lightbulb.SlashCommand)
async def log10(context):
    num = context.options.num
    if num <= 0:
        await context.respond("You can't compute the logarithm of a nonpositive number!")
    else:
        await context.respond(math.log10(num))

# /combinations [n = int] [k = int]
@bot.command
@lightbulb.option('k', 'number of items to chose', type=int)
@lightbulb.option('n', 'total number of items', type=int)
@lightbulb.command('combinations', 'Computes the number of combinations to pick k items from n total items')
@lightbulb.implements(lightbulb.SlashCommand)
async def comb(context):
    n = context.options.n
    k = context.options.k
    if n <= 0:
        await context.respond('The number of items to chose needs to be positive!')
    elif k <= 0:
        await context.respond('The total number of items needs to be positive!')
    else:
        await context.respond(math.comb(n, k))

# /permutations [n = int] [k = int]
@bot.command
@lightbulb.option('k', 'number of items to chose', type=int)
@lightbulb.option('n', 'total number of items', type=int)
@lightbulb.command('combinations', 'Computes the number of permutations to pick k items from n total items')
@lightbulb.implements(lightbulb.SlashCommand)
async def perm(context):
    n = context.options.n
    k = context.options.k
    if n <= 0:
        await context.respond('The number of items to chose needs to be positive!')
    elif k <= 0:
        await context.respond('The total number of items needs to be positive!')
    else:
        await context.respond(math.perm(n, k))

# /gcd [num1 = int] [num2 = int]
@bot.command
@lightbulb.option('num2', 'second number', type=int)
@lightbulb.option('num1', 'first number', type=int)
@lightbulb.command('combinations', 'Computes the number of combinations to pick k items from n total items')
@lightbulb.implements(lightbulb.SlashCommand)
async def gcd(context):
    num1 = context.options.num1
    num2 = context.options.num2
    await context.respond(math.gcd(num1, num2))

# /lcm [num1 = int] [num2 = int]
@bot.command
@lightbulb.option('num2', 'second number', type=int)
@lightbulb.option('num1', 'first number', type=int)
@lightbulb.command('combinations', 'Computes the number of combinations to pick k items from n total items')
@lightbulb.implements(lightbulb.SlashCommand)
async def lcm(context):
    num1 = context.options.num1
    num2 = context.options.num2
    await context.respond(math.lcm(num1, num2))

# /deg [num = float]
@bot.command
@lightbulb.option('degrees', 'degrees', type=float)
@lightbulb.command('deg', 'Converts radians to degrees')
@lightbulb.implements(lightbulb.SlashCommand)
async def deg(context):
    await context.respond(math.degrees(context.options.degrees))

# /rad [num = float]
@bot.command
@lightbulb.option('radians', 'radians', type=float)
@lightbulb.command('rad', 'Converts degrees to radians')
@lightbulb.implements(lightbulb.SlashCommand)
async def rad(context):
    await context.respond(math.radians(context.options.radians))

# /sin [num = float] [rad = bool]
@bot.command
@lightbulb.option('rad', 'True: radians; False: degrees', type=bool)
@lightbulb.option('num', 'the degrees/radians', type=float)
@lightbulb.command('sin', 'Computes the sine of the inputted degree/radians')
@lightbulb.implements(lightbulb.SlashCommand)
async def sin(context):
    num = context.options.num
    rad = context.options.rad
    if not rad:
        num = math.radians(num)
    await context.respond(math.sin(num))

# /cos [num = float] [rad = bool]
@bot.command
@lightbulb.option('rad', 'True: radians; False: degrees', type=bool)
@lightbulb.option('num', 'the degrees/radians', type=float)
@lightbulb.command('cos', 'Computes the cosine of the inputted degree/radians')
@lightbulb.implements(lightbulb.SlashCommand)
async def cos(context):
    num = context.options.num
    rad = context.options.rad
    if not rad:
        num = math.radians(num)
    await context.respond(math.cos(num))

# /tan [num = float] [rad = bool]
@bot.command
@lightbulb.option('rad', 'True: radians; False: degrees', type=bool)
@lightbulb.option('num', 'the degrees/radians', type=float)
@lightbulb.command('tan', 'Computes the tangent of the inputted degree/radians')
@lightbulb.implements(lightbulb.SlashCommand)
async def tan(context):
    num = context.options.num
    rad = context.options.rad
    if not rad:
        num = math.radians(num)
    if math.cos(num) == 0:
        await context.respond("You can't compute the tangent of that value!")
    else:
        await context.respond(math.tan(num))

# /csc [num = float] [rad = bool]
@bot.command
@lightbulb.option('rad', 'True: radians; False: degrees', type=bool)
@lightbulb.option('num', 'the degrees/radians', type=float)
@lightbulb.command('csc', 'Computes the cosecant of the inputted degree/radians')
@lightbulb.implements(lightbulb.SlashCommand)
async def csc(context):
    num = context.options.num
    rad = context.options.rad
    if not rad:
        num = math.radians(num)
    if math.sin(num) == 0:
        await context.respond("You can't compute the cosecant of that value!")
    else:
        await context.respond(1 / math.sin(num))

# /sec [num = float] [rad = bool]
@bot.command
@lightbulb.option('rad', 'True: radians; False: degrees', type=bool)
@lightbulb.option('num', 'the degrees/radians', type=float)
@lightbulb.command('sec', 'Computes the secant of the inputted degree/radians')
@lightbulb.implements(lightbulb.SlashCommand)
async def sec(context):
    num = context.options.num
    rad = context.options.rad
    if not rad:
        num = math.radians(num)
    if math.cos(num) == 0:
        await context.respond("You can't compute the secant of that value!")
    else:
        await context.respond(1 / math.cos(num))

# /cot [num = float] [rad = bool]
@bot.command
@lightbulb.option('rad', 'True: radians; False: degrees', type=bool)
@lightbulb.option('num', 'the degrees/radians', type=float)
@lightbulb.command('cot', 'Computes the cotangent of the inputted degree/radians')
@lightbulb.implements(lightbulb.SlashCommand)
async def cot(context):
    num = context.options.num
    rad = context.options.rad
    if not rad:
        num = math.radians(num)
    if math.sin(num) == 0:
        await context.respond("You can't compute the cotangent of that value!")
    else:
        await context.respond(math.cos(num) / math.sin(num))

# /asin [num = float] [rad = bool]
@bot.command
@lightbulb.option('rad', 'True: radians; False: degrees', type=bool)
@lightbulb.option('num', 'the degrees/radians', type=float)
@lightbulb.command('asin', 'Computes the inverse sine of the inputted value')
@lightbulb.implements(lightbulb.SlashCommand)
async def asin(context):
    num = context.options.num
    rad = context.options.rad
    if not rad:
        num = math.radians(num)
    await context.respond(math.asin(num))

# /acos [num = float] [rad = bool]
@bot.command
@lightbulb.option('rad', 'True: radians; False: degrees', type=bool)
@lightbulb.option('num', 'the degrees/radians', type=float)
@lightbulb.command('acos', 'Computes the inverse cosine of the inputted value')
@lightbulb.implements(lightbulb.SlashCommand)
async def acos(context):
    num = context.options.num
    rad = context.options.rad
    if not rad:
        num = math.radians(num)
    await context.respond(math.acos(num))

# /atan [num = float] [rad = bool]
@bot.command
@lightbulb.option('rad', 'True: radians; False: degrees', type=bool)
@lightbulb.option('num', 'the degrees/radians', type=float)
@lightbulb.command('atan', 'Computes the inverse tangent of the inputted value')
@lightbulb.implements(lightbulb.SlashCommand)
async def atan(context):
    num = context.options.num
    rad = context.options.rad
    if not rad:
        num = math.radians(num)
    await context.respond(math.atan(num))

# /pi
@bot.command
@lightbulb.command('pi', 'displays the value of pi')
@lightbulb.implements(lightbulb.SlashCommand)
async def pi(context):
    await context.respond(math.pi)

# /e
@bot.command
@lightbulb.command('e', 'displays the value of e')
@lightbulb.implements(lightbulb.SlashCommand)
async def e(context):
    await context.respond(math.e)

def valid_float_list(entry):
    return isinstance(entry, list) and all(isinstance(el, float) or isinstance(el, int) for el in entry)

def invalid_float_list():
    return 'That is not a valid input! Please have your input in a form like this: [1, -2, 3.4]'

# /mean [num = array<float>]
@bot.command
@lightbulb.option('nums', 'numbers')
@lightbulb.command('mean', 'Computes the mean of a list of numbers')
@lightbulb.implements(lightbulb.SlashCommand)
async def mean(context):
    nums = context.options.nums
    if not valid_float_list(nums):
        await context.respond(invalid_float_list())
        return
    await context.respond(stats.mean(nums))

# /median [num = array<float>]
@bot.command
@lightbulb.option('nums', 'numbers')
@lightbulb.command('median', 'Computes the median of a list of numbers')
@lightbulb.implements(lightbulb.SlashCommand)
async def median(context):
    nums = context.options.nums
    if not valid_float_list(nums):
        await context.respond(invalid_float_list())
        return
    await context.respond(stats.median(nums))

# /mode [num = array<float>]
@bot.command
@lightbulb.option('nums', 'numbers')
@lightbulb.command('mode', 'Computes the mode of a list of numbers')
@lightbulb.implements(lightbulb.SlashCommand)
async def mode(context):
    nums = context.options.nums
    if not valid_float_list(nums):
        await context.respond(invalid_float_list())
        return
    await context.respond(stats.mode(nums))

# /quantiles [num = array<float>] [split = int]
@bot.command
@lightbulb.option('split', 'number of quantiles', type=int)
@lightbulb.option('nums', 'numbers')
@lightbulb.command('quantiles', 'Computes the quantiles of a list of numbers')
@lightbulb.implements(lightbulb.SlashCommand)
async def quantiles(context):
    nums = context.options.nums
    split = context.options.split
    if not valid_float_list(nums):
        await context.respond(invalid_float_list())
        return
    if split <= 0:
        await context.respond('Please chose a positive value for the number of quantiles!')
    else:
        await context.respond(stats.stdev(nums, split))

# /std [num = array<float>]
@bot.command
@lightbulb.option('nums', 'numbers')
@lightbulb.command('std', 'Computes the standard deviation of a list of numbers')
@lightbulb.implements(lightbulb.SlashCommand)
async def std(context):
    nums = context.options.nums
    if not valid_float_list(nums):
        await context.respond(invalid_float_list())
        return
    await context.respond(stats.stdev(nums))

# /var [num = array<float>]
@bot.command
@lightbulb.option('nums', 'numbers', type=int)
@lightbulb.command('var', 'Computes the variance of a list of numbers')
@lightbulb.implements(lightbulb.SlashCommand)
async def var(context):
    nums = context.options.nums
    if not valid_float_list(nums):
        await context.respond(invalid_float_list())
        return
    await context.respond(stats.variance(nums))

def is_prime(num):
    if num > 1:
        for i in range(2, int(math.sqrt(num)) + 1):
            if (num % i) == 0:
                return False
    return True

# /isprime [num = int]
@bot.command
@lightbulb.option('num', 'number', type=int)
@lightbulb.command('isprime', 'Checks if the number is prime')
@lightbulb.implements(lightbulb.SlashCommand)
async def isprime(context):
    num = context.options.num
    if is_prime(num):
        await context.respond(str(num) + " is a prime number!")
    await context.respond(str(num) + " is not a prime number!")

# /factors [num = int]

# /primefactors [num = int]

# /primes [max = int]

# /primegaps [max = int]

# /solve_quadratic [a = float] [b = float] [c = float]

# /degrees_of_a_sided_figure [sides = int]

def collatz_conjecture(num):
    seq = [num]
    while num != 1:
        if num % 2:
            num = 3 * num + 1 
        else:
            num //= 2
        seq.append(num)
    return seq

# /collatznum [num = int]
@bot.command
@lightbulb.option('num', 'number', type=int)
@lightbulb.command('collatz', 'Computes a collatz conjecture sequence')
@lightbulb.implements(lightbulb.SlashCommand)
async def collatzseq(context):
    num = context.options.num
    if num <= 0:
        await context.respond('Please enter a positive number!')
        return
    seq = collatz_conjecture(num)
    val = len(seq)
    await context.respond(val)

# /collatzseq [num = int]
@bot.command
@lightbulb.option('num', 'number', type=int)
@lightbulb.command('collatz', 'Computes a collatz conjecture sequence')
@lightbulb.implements(lightbulb.SlashCommand)
async def collatzseq(context):
    num = context.options.num
    if num <= 0:
        await context.respond('Please enter a positive number!')
        return
    val = collatz_conjecture(num)
    await context.respond(val)

bot.run()