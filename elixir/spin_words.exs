defmodule Spin do
  def spin_words(message) do
  message
  |> String.split(" ")
  |> Enum.map(fn word ->
      if String.length(word) >= 5 do
        String.reverse(word)
      else
        word
      end
    end)
  |> Enum.join(" ")
  end
end

IO.puts(Spin.spin_words("Let me hear the battle cry"))
