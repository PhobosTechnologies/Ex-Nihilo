import numpy

# Ex Nihilo
#
# 	    Maybe give it a split-base: 2, or 3, or 4, or 5? ... (how many interactive charges break from nothingness)
# 	    allow to split and charge x-many generations out.
# 	    then analyze generation interactivity?


# === ReactionChamber ==================================================================================================
class ReactionChamber:
	"""
	ReactionChamber()
		Starts the NihiloSplit chain reaction
		Analyzes possible interactivity among spawn
	"""

	def __init__(self, iterations, spawn_seed):
		self.lineage = dict()
		self.iterations = range(iterations)
		self.spawn_seed = spawn_seed + 1 # adding 1 to account for the zero-slip in range()

	# === NihiloSplit ==================================================================================================
	class NihiloSplit:
		"""
		NihiloSplit()

		PARAMETERS:
			mother              : mother's self.id
			id                  : iteration + harmonic_disunion (aka: "charge")
			spawn_seed          : how many siblings are born together at each iteration (experiment later with oscillating spawn_seed)
			harmonic_disunion   : (aka: "charge") the poly-vector interactive properties derived from spawn_seed.
									If the spawn_seed is 2, then there are only two polar charges. If the spawn_seed is 3, then there are
									3 interactive polar charges - one for each new spawn.

				*** later, consider assigning attributes to each charge from which the interactive polar mechanics are derived.
					ie i        : bipolar interactive system of CC and CCW spin along some axis.
					ie ii       : Vibration (size pulse / directional pulse / angular pulse), etc.

			iteration           : the count of each generation of "particle" splits
			sibling_ids         : (maybe add this later - a list so each family from each generation is aware of its siblings
		"""
		def __init__(self, iteration, harmonic_disunion=None):
			self.mother = iteration - 1
			self.generation = iteration
			self.harmonic_disunion = harmonic_disunion

			if self.mother == -1:
				self.id = int(0)
			elif self.mother >= 0:
				self.id = self.mother + 1

			rc.lineage[f'{self.id}.{self.harmonic_disunion}'] = self

	# === END: NihiloSplit =============================================================================================

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
		rc.NihiloSplit(0, self.spawn_seed)

		for iteration in self.iterations:
			_A = ord('a')
			for disunion in range(_A, _A + self.spawn_seed):
				rc.NihiloSplit(iteration, chr(disunion))

	def display_lineage(self):
		for i in self.iterations:
			_A = ord('a')
			for disunion_harmonic in range(_A, _A + self.spawn_seed):
				ns = self.lineage[f'{i}.{chr(disunion_harmonic)}']
				print(f'{ns.mother}.{ns.generation}.{ns.harmonic_disunion}')

		# for split in self.lineage:
		# 	print(f'{split}')
# === END: ReactionChamber =============================================================================================


# ReactionChamber(iterations, spawn_seed)
rc = ReactionChamber(5, 3)
rc.om()
rc.display_lineage()
