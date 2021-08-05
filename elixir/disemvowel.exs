defmodule Kata do
  def disemvowel(s) do
    vowels = ["e", "u", "i", "o", "a", "E", "U", "I", "O", "A"]
    s
    |> String.replace(vowels, "")
  end
end
