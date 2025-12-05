program solution
use sol_mod, only: read_input, part_one, part_two
implicit none

character(len=*), parameter :: file = 'input.txt'

call read_input(file)

print *, 'part one: ', part_one()
print *, 'part two: ', part_two()

end program solution