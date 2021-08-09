defmodule Kata do
    def clean_string(s) do
        cond do
            :nomatch == :binary.match(s, "#") -> s
            String.first(s) == "#" -> clean_string(String.replace(s, ~r/^#/, ""))
            true -> clean_string(String.replace(s, ~r/[^#]#/, ""))
        end
    end
end

IO.puts Kata.clean_string "##aaaaaa####d#dd#"