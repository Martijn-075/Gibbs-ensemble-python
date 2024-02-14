import param

def energy(R2, RC2):
    en = 0.
    vir = 0.

    if R2 < RC2:
        R2i = param.SIGMA2 / R2
        R6i = R2i * R2i *R2i
        en = param.EPSX4 * (R6i * R6i - R6i)

        vir = param.EPSX48 * (R6i * R6i - 0.5 * R6i)
    
    return en, vir

def energy_particle(particles, particle):
    part_en = 0.
    part_vir = 0.
    for part in particles:
        if part != particle:
            dx = particle.x - part.x
            dy = particle.y - part.y
            dz = particle.z - part.z

            R2P = dx * dx + dy * dy + dz * dz

            en, vir = energy(R2P, 200.)

            part_en += en
            part_vir += vir

    return part_en, part_vir

def energy_total(particles):
    total_en = 0.
    total_vir = 0.
    for particle in particles:
        en, vir = energy_particle(particles, particle)
        total_en += en
        total_vir += vir
    
    return total_en, total_vir
