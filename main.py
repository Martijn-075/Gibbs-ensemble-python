import param
import energy
import particle

particles = []
for i in range(param.N):
    particles.append(particle.particle())

particles[1].x = 0.5


en = 0.
vir = 0.
en, vir = energy.energy_total(particles)

print(en, vir)
