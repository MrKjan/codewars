defmodule Dioph do
  def sol_equa(n) do
    for a <- 1..trunc(:math.sqrt(n)),
        rem(n, a) == 0,
        b = div(n, a),
        x = div(a + b, 2),
        y = div(b - a, 4),
        x*x - 4*y*y == n do
      {x, y}
    end
  end
end