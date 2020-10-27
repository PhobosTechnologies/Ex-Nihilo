iterations = 5
charge_split = 3

particle_family_tree = dict()
siblings = list()


class ReactionChamber:

	def __init__(self):
		self.first_generation()

	def first_generation(self):
		particle_family_tree['0.0'] = self.Particle('Void', '0.0', 1)

	class Particle:

		def __init__(self, mother, particle_id, generation, charge=None):
			self.iterations = iterations
			self.charge_split = charge_split
			self.mother = mother
			self.id = particle_id
			self.generation = generation
			self.charge = charge

			if self.generation <= self.iterations:
				self.generate_particles()

		def generate_particles(self):

			for charge in range((_ := ord('a')), (_ + self.charge_split)):
				particle_id = f'{self.id}:{self.generation}.{charge}'
				new_gen = self.generation + 1
				particle_family_tree[particle_id] = ReactionChamber.Particle(self.id, particle_id, new_gen, charge)


def display_particles():
	# print(particle_family_tree)
	for particle in particle_family_tree:
		print(particle)


def display_particle_lineage():
	for iteration in range(1, iterations+1):
		for charge in range((_ := ord('a')), (_ + charge_split)):
			particle_id = f'{iteration}.{charge}'
			siblings.append(particle_family_tree[particle_id])
		print(siblings)


rc = ReactionChamber()
# display_particle_lineage()
display_particles()
