from dotenv import load_dotenv
load_dotenv()

from langchain_core import __version__ as core_version
from importlib.metadata import version as pkg_version
lg_version = pkg_version("langgraph")

from langchain_anthropic import ChatAnthropic

print(f"langchain-core version: {core_version}")
print(f"langgraph version: {lg_version}")

print(f"langchain-openai version: {pkg_version('langchain-openai')}")


def main():
    llm_anthropic = ChatAnthropic(model="claude-sonnet-4-5-20250929", temperature=0)
    response_anthropic = llm_anthropic.invoke("Say 'Setup complete!' in 1 word")
    print(f"Anthropic response: {response_anthropic}")

    print("Setup complete!")


if __name__ == "__main__":
    main()
