# Ex Nihilo
#
# 	    Maybe give it a split-base: 2, or 3, or 4, or 5? ... (how many interactive charges break from nothingness)
# 	    allow to split and charge x-many generations out.
# 	    then analyze generation interactivity?
#
#

class NihiloSplit:
	"""
    PARAMETERS:
        mother: mother's spawn id
        self_ID: spawn_id + charge
        spawn_seed: how many siblings are born together at each iteration (experiment later with oscillating spawn_seed)
        charge ... perhaps the charge can be encoded into the ID, ie: pos/neg - up/dn - lft/rt - ... etc.
            so an id could be neg-up-rt which also inherently represents its charge.
            ** now or later - assign attributes to each charge with which interactions are initiated
                ie: CC and CCW spin along X axis. Vibration (size pulse / directional pulse / angular pulse)
                , direction (xyz), make-believe forces ... or is this going to create it's own forces?
		generation ... generation can also be derived from ID, in that first gen will have
			a single charge type, second gen will have two charge types.
        sibling_IDs (list)
	"""
	def __init__(self, mother, iterations, spawn_seed, harmonic_disunion=None):
		self.mother = mother
		self.iteration = iterations - 1
		self.harmonic_disunion = harmonic_disunion

		if self.mother is None:
			print("mama is None")
			self.id = int(0)
		elif type(self.mother) is int:
			self.id = self.mother + 1

		print(f'ID: {self.id} - mother: {self.mother} - iteration: {self.iteration} - charge: {self.harmonic_disunion}')

		if self.iteration > 0:
			_A = ord('a')
			for disunion in range(_A, _A+spawn_seed):

				NihiloSplit(self.mother, self.iteration, spawn_seed, chr(disunion))


class ReactionChamber:
	"""
	ReactionChamber
		Starts the NihiloSplit chain reaction
		Analyzes possible interactivity among spawn
	"""
	def __init__(self, iterations, spawn_seed):
		self.iterations = iterations
		self.spawn_seed = spawn_seed + 1 # adding 1 to account for the zero-slip in range()

	# "sings" it all into existence - kicks off the NS chain reaction
	def om(self):

		# design naming scheme to feed into the split
		# how do different numbers of charges in each scheme interact with each other?
		#   ie: 3: a, b, and c.
		#       a attract b / a+b repels c
		#       b attract c / b+c repels a
		#       c attract a / c+a repels b ... this sort of thing ... is there a logical method for assigning such properties?
		#                                       something, perhaps, born from the mechanics of the split? ... think about this
		# For now, just rely on the idea that all three charges are equal (when together) to their mother's full charge
		# Each iteration's number is to be used as the base-property, then use lowercase letters in order to represent
		# the separate charges according to the spawn_seed.

		# let there be light mother fucker!
		ns = NihiloSplit(None, self.iterations, self.spawn_seed)


# ReactionChamber(iterations, spawn_seed)
rc = ReactionChamber(3, 3)
rc.om()
