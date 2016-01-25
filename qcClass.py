__author__ = 'vikram'

words = ["there", "are", "some", "words"]
print " ".join(words)

favFruits = ["banana", "mango", "papaya", "apple", "pineapple"]
print favFruits[len(favFruits) - 3:len(favFruits)]


def vowel_names(names):
    output_names = []
    for name in names:
        if name[0].upper() in ['A', 'E', 'I', 'O', 'U']:
            output_names.append(name)
    return output_names
names = ["Scott", "Arthur", "Jan", "Elizabeth"]
print vowel_names(names)

declInd = '''Action of Second Continental Congress,\nJuly 4, 1776.\nThe unanimous Declaration of the thirteen united States of America,\n\nWHEN in the Course of human Events, it becomes necessary for one People to dissolve the Political Bands which have connected them with another, and to assume among the Powers of the Earth, the separate and equal Station to which the Laws of Nature and of Nature\xe2\x80\x99s God entitle them, a decent Respect to the Opinions of Mankind requires that they should declare the causes which impel them to the Separation.\n\nWE hold these Truths to be self-evident, that all Men are created equal, that they are endowed by their Creator with certain unalienable Rights, that among these are Life, Liberty, and the Pursuit of Happiness\xe2\x80\x94That to secure these Rights, Governments are instituted among Men, deriving their just Powers from the Consent of the Governed, that whenever any form of Government becomes destructive of these Ends, it is the Right of the People to alter or to abolish it, and to institute new Government, laying its Foundation on such Principles, and organizing its Powers in such form, as to them shall seem most likely to effect their Safety and Happiness. Prudence, indeed, will dictate that Governments long established should not be changed for light and transient Causes; and accordingly all Experience hath shewn, that Mankind are more disposed to suffer, while Evils are sufferable, than to right themselves by abolishing the forms to which they are accustomed. But when a long Train of Abuses and Usurpations, pursuing invariably the same Object, evinces a Design to reduce them under absolute Despotism, it is their Right, it is their Duty, to throw off such Government, and to provide new Guards for their future Security. Such has been the patient Sufferance of these Colonies; and such is now the Necessity which constrains them to alter their former Systems of Government. The History of the present King of Great-Britain is a History of repeated Injuries and Usurpations, all having in direct Object the Establishment of an absolute Tyranny over these States. To prove this, let Facts be submitted to a candid World.\n\nHe has refused his Assent to Laws, the most wholesome and necessary for the public Good.\n\nHe has forbidden his Governors to pass Laws of immediate and pressing Importance, unless suspended in their Operation till his Assent should be obtained; and when so suspended, he has utterly neglected to attend to them.\n\nHe has refused to pass other Laws for the Accommodation of large Districts of People, unless those People would relinquish the Right of Representation in the Legislature, a Right inestimable to them, and formidable to Tyrants only.\n\nHe has called together Legislative Bodies at Places unusual, uncomfortable, and distant from the Depository of their public Records, for the sole Purpose of fatiguing them into Compliance with his Measures.\n\nHe has dissolved Representative Houses repeatedly, for opposing with manly Firmness his Invasions on the Rights of the People.\n\nHe has refused for a long Time, after such Dissolutions, to cause others to be elected; whereby the Legislative Powers, incapable of Annihilation, have returned to the People at large for their exercise; the State remaining in the mean time exposed to all the Dangers of Invasion from without, and Convulsions within.\n\nHe has endeavoured to prevent the Population of these States; for that Purpose obstructing the Laws for Naturalization of foreigners; refusing to pass others to encourage their Migrations hither, and raising the Conditions of new Appropriations of Lands.\n\nHe has obstructed the Administration of Justice, by refusing his assent to Laws for establishing Judiciary Powers.\n\nHe has made Judges dependent on his Will alone, for the Tenure of their Offices, and the Amount and Payment of their Salaries.\n\nHe has erected a Multitude of new Offices, and sent hither Swarms of Officers to harrass our People, and eat out their Substance.\n\nHe has kept among us, in Times of Peace, Standing Armies, without the consent of our Legislatures.\n\nHe has affected to render the Military independent of and superior to the Civil Power.\n\nHe has combined with others to subject us to a Jurisdiction foreign to our Constitution, and unacknowledged by our Laws; giving his Assent to their Acts of pretended Legislation:\n\nFor quartering large Bodies of Armed Troops among us:\n\nFor protecting them, by a mock Trial, from Punishment for any Murders which they should commit on the Inhabitants of these States:\n\nFor cutting off our Trade with all Parts of the World:\n\nFor imposing Taxes on us without our Consent:\n\nFor depriving us, in many Cases, of the Benefits of Trial by Jury:\n\nFor transporting us beyond Seas to be tried for pre-tended Offences:\n\nFor abolishing the free System of English Laws in a neighbouring Province, establishing therein an arbitrary Government and enlarging its Boundaries, so as to render it at once an Example and fit Instrument for introducing the same absolute Rule into these Colonies:\n\nFor taking away our Charters, abolishing our most valuable Laws, and altering fundamentally the forms of our Governments:\n\nFor suspending our own Legislatures, and declaring themselves invested with Power to legislate for us in all Cases whatsoever.\n\nHe has abdicated Government here, by declaring us out of his Protection and waging War against us.\n\nHe has plundered our Seas, ravaged our Coasts, burnt our Towns, and destroyed the Lives of our People.\n\nHe is, at this Time, transporting large Armies of foreign Mercenaries to compleat the Works of Death, Desolation, and Tyranny already begun with circumstances of Cruelty and Perfidy, scarcely paralleled in the most barbarous Ages, and totally unworthy of the Head of a civilized Nation.\n\nHe has constrained our fellow Citizens taken Captive on the high Seas to bear Arms against their Country, to become the Executioners of their friends and Brethren, or to fall themselves by their Hands.\n\nHe has excited domestic Insurrections amongst us, and has endeavoured to bring on the Inhabitants of our Frontiers, the merciless Indian Savages, whose known Rule of Warfare, is an undistinguished Destruction, of all Ages, Sexes and Conditions.\n\nIn every stage of these Oppressions we have Petitioned for Redress in the most humble Terms: Our repeated Petitions have been answered only by repeated Injury. A Prince, whose Character is thus marked by every act which may define a Tyrant, is unfit to be the Ruler of a free People.\n\nNor have we been wanting in Attentions to our British Brethren. We have warned them from Time to Time of Attempts by their Legislature to extend an unwarrantable jurisdiction over us. We have reminded them of the Circumstances of our Emigration and Settlement here. We have appealed to their native justice and Magnanimity, and we have conjured them by the Ties of our common Kindred to disavow these Usurpations, which, would inevitably interrupt our Connections and Correspondence. They too have been deaf to the Voice of Justice and of Consanguinity. We must, therefore, acquiesce in the Necessity, which denounces our Separation, and hold them, as we hold the rest of Mankind, Enemies in War, in Peace, Friends.\n\nWe, therefore, the Representatives of the UNITED STATES OF AMERICA, in General Congress, Assembled, appealing to the Supreme Judge of the World for the Rectitude of our Intentions, do, in the Name, and by Authority of the good People of these Colonies, solemnly Publish and Declare, That these United Colonies are, and of Right ought to be, FREE AND INDEPENDENT STATES, that they are absolved from all Allegiance to the British Crown, and that all political Connection between them and the State of Great-Britain, is and ought to be totally dissolved; and that as FREE AND INDEPENDENT STATES, they have full Power to levy War, conclude Peace, contract Alliances, establish Commerce, and to do all other Acts and Things which INDEPENDENT STATES may of right do. And for the support of this Declaration, with a firm Reliance on the Protection of divine Providence, we mutually pledge to each other our Lives, our fortunes, and our sacred Honor.'
'''
for word in declInd.split(" "):
    #if ('x' in word) or ('X' in word):
    if 'x' in word.lower():
        print word.strip(";.'")
capList = []
for x in declInd:
    if x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        capList.append(x)
print capList[373:384]

def flip_dict(myDict):
    assert isinstance(myDict, dict)
    print myDict
    newkey = []
    newval = []
    for item in myDict:
        newval.append(item)
        newkey.append(myDict[item])
    print zip(newkey, newval)  # used to create a list of tuples
    return dict(zip(newkey, newval))

myDict = {'one': 1, 'two': 2, 'three': 3}
reversedDict = flip_dict(myDict)
print reversedDict

routes = {101: ("Tumwater, Washington", "Los Angeles, California"),
          66: ("Chicago, Illinois", "Santa Monica, California"),
          95: ("Miami, FL", "Sometown, Maine")}

print routes
start = ""
dest = ""
outStr = ""
for item in routes:
    start, dest = routes[item]
    print "Route %d goes from %s to %s" % (item, start, dest)

numbers = range(1, 10)
print list(enumerate(numbers))  # enumerate makes a list of tuples

