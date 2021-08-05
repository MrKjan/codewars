defmodule Rec2sq do
  def squares_in_rect(l, w) when l == w, do: nil
  def squares_in_rect(l, w), do: loop(l, w, []) |> Enum.reverse
  def loop(a, b, ret) when a == b, do: [a | ret]
  def loop(a, b, ret) when a > b, do: loop(a-b, b, [b | ret])
  def loop(a, b, ret), do: loop(a, b-a, [a | ret])
end
