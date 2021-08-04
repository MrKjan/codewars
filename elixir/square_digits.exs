defmodule Kata do
  def square_digits(n) do
      for digit <- Integer.digits(n), do: digit * digit
      |> List.foldl("", &(&2 <> Integer.to_string(&1)))
      |> String.to_integer
  end
end
