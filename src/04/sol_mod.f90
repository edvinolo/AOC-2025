module sol_mod
implicit none

integer, parameter :: max_len = 1000
character(len=max_len) :: in_line
character(len=:), allocatable :: line

logical, allocatable :: grid(:,:)
logical, allocatable :: grid_new(:,:)
integer :: n_grid, m_grid

contains

subroutine read_input(file)
    character(len=*), intent(in) :: file

    integer :: unit, ios
    integer :: n_lines,m
    integer :: i,j

    open(file=file, newunit=unit,iostat = ios, action='read')

    n_lines = 0
    ios = 0

    do while(ios==0)
        read(unit,'(a)',iostat=ios) in_line
        line = trim(in_line)
        if (n_lines == 0) m = len(line)
        n_lines = n_lines + 1
    end do
    n_lines = n_lines - 1

    n_grid = n_lines+2
    m_grid = m + 2
    allocate(grid(m_grid,n_grid),source = .false.)

    rewind(unit)

    do i = 1,n_lines
        read(unit,'(a)') in_line
        line = trim(in_line)
        do j = 1,m
            grid(j+1,i+1) = is_paper(line(j:j))
        end do
    end do

    grid_new = grid

    close(unit)

end subroutine read_input

integer function part_one() result(res)
    integer :: i,j

    res = 0
    do i = 2,n_grid-1
        do j = 2,n_grid-1
            if (grid(j,i)) then
                if (accessible(j,i)) then
                    res = res + 1
                    grid_new(j,i) = .false.
                end if
            end if
        end do
    end do

end function part_one

integer function part_two() result(res)
    logical :: keep_going
    integer :: removed

    res = 0
    keep_going = .true.
    do while(keep_going)
        removed = part_one()
        if (removed > 0) then
            res = res + removed
            grid = grid_new
        else
            keep_going = .false.
        end if
    end do

end function part_two

logical function accessible(j,i) result(res)
    integer, intent(in) :: i,j

    integer :: l,k
    integer :: counter

    counter = 0
    do l = -1,1
        do k = -1,1
            if (grid(j+k,i+l)) counter = counter + 1
        end do
    end do

    res = (counter < 5)
end function accessible

logical function is_paper(x) result(res)
    character, intent(in) :: x

    res = (x == '@')

end function is_paper

end module sol_mod