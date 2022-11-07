import hikari
import lightbulb
import math

bot = lightbulb.BotApp(
    token = , # REDACTED
    default_enabled_guilds = ()   # REDACTED
    )

# ADD EXTENSIONS

# Basic Operations

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

# $$$ /deg [num]

# $$$ /rad [num]

# $$$ /sin [num] [rad]

# $$$ /cos [num] [rad]

# $$$ /tan [num] [rad]

# $$$ /csc [num] [rad]

# $$$ /sec [num] [rad]

# $$$ /cot [num] [rad]

# $$$ /asin [num] [rad]

# $$$ /acos [num] [rad]

# $$$ /atan [num] [rad]

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

# /factors [num]

# /primefactors [num]

# /mean [num]

# /median

# /mode

# /std

# /var

# /solve_quadratic

# /degrees_of_a_sided_figure

# / collatz_conjecture


bot.run()