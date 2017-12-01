"""
--- Day 1: Inverse Captcha ---

The night before Christmas, one of Santa's Elves calls you in a panic. "The
printer's broken! We can't print the Naughty or Nice List!" By the time you
make it to sub-basement 17, there are only a few minutes until midnight. "We
have a big problem," she says; "there must be almost fifty bugs in this system,
but nothing else can print The List. Stand in this square, quick! There's no
time to explain; if you can convince them to pay you in stars, you'll be able
to--" She pulls a lever and the world goes blurry.

When your eyes can focus again, everything seems a lot more pixelated than
before. She must have sent you inside the computer! You check the system clock:
    25 milliseconds until midnight. With that much time, you should be able to
    collect all fifty stars by December 25th.

    Collect stars by solving puzzles. Two puzzles will be made available on
    each day millisecond in the advent calendar; the second puzzle is unlocked
    when you complete the first. Each puzzle grants one star. Good luck!

    You're standing in a room with "digitization quarantine" written in LEDs
    along one wall. The only door is locked, but it includes a small interface.
    "Restricted Area - Strictly No Digitized Users Allowed."

    It goes on to explain that you may only leave by solving a captcha to prove
    you're not a human. Apparently, you only get one millisecond to solve the
    captcha: too fast for a normal human, but it feels like hours to you.

    The captcha requires you to review a sequence of digits (your puzzle input)
    and find the sum of all digits that match the next digit in the list. The
    list is circular, so the digit after the last digit is the first digit in
    the list.

    For example:

        1122 produces a sum of 3 (1 + 2) because the first digit (1) matches
        the second digit and the third digit (2) matches the fourth digit.
        1111 produces 4 because each digit (all 1) matches the next.
        1234 produces 0 because no digit matches the next.
        91212129 produces 9 because the only digit that matches the next one is
        the last digit, 9.
        What is the solution to your captcha?
"""

tests = (
    ('1122', 3),
    ('1111', 4),
    ('1234', 0),
    ('91212129', 9),
    ('428122498997587283996116951397957933569136949848379417125362532269869461185743113733992331379856446362482129646556286611543756564275715359874924898113424472782974789464348626278532936228881786273586278886575828239366794429223317476722337424399239986153675275924113322561873814364451339186918813451685263192891627186769818128715595715444565444581514677521874935942913547121751851631373316122491471564697731298951989511917272684335463436218283261962158671266625299188764589814518793576375629163896349665312991285776595142146261792244475721782941364787968924537841698538288459355159783985638187254653851864874544584878999193242641611859756728634623853475638478923744471563845635468173824196684361934269459459124269196811512927442662761563824323621758785866391424778683599179447845595931928589255935953295111937431266815352781399967295389339626178664148415561175386725992469782888757942558362117938629369129439717427474416851628121191639355646394276451847131182652486561415942815818785884559193483878139351841633366398788657844396925423217662517356486193821341454889283266691224778723833397914224396722559593959125317175899594685524852419495793389481831354787287452367145661829287518771631939314683137722493531318181315216342994141683484111969476952946378314883421677952397588613562958741328987734565492378977396431481215983656814486518865642645612413945129485464979535991675776338786758997128124651311153182816188924935186361813797251997643992686294724699281969473142721116432968216434977684138184481963845141486793996476793954226225885432422654394439882842163295458549755137247614338991879966665925466545111899714943716571113326479432925939227996799951279485722836754457737668191845914566732285928453781818792236447816127492445993945894435692799839217467253986218213131249786833333936332257795191937942688668182629489191693154184177398186462481316834678733713614889439352976144726162214648922159719979143735815478633912633185334529484779322818611438194522292278787653763328944421516569181178517915745625295158611636365253948455727653672922299582352766484',
     1034),
)

def inverse_captcha(input_sequence):
    digits = [int(c) for c in input_sequence]
    # We start with element 1 in the list and end with element 0, so just
    # preload.
    captcha_value = 0
    digits_length = len(digits)
    lookahead_offset = 1

    for idx in xrange(digits_length):
        # Modulo to make sure we step around to item 0 in the list.
        lookahead_idx = (idx + lookahead_offset) % digits_length
        digit = digits[idx]
        lookahead_digit = digits[lookahead_idx]
        if digit == lookahead_digit:
            captcha_value += digit
    return captcha_value

if __name__ == "__main__":
    for input_seq, expected_output in tests:
        actual_output = inverse_captcha(input_seq)
        assert actual_output == expected_output, "{0} did not equal {1}".format(
            actual_output,
            expected_output
        )
    print "All Tests Passed!"
