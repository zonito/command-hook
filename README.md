Command Hook Pre-Commit
=======================
Hook any unit test / set up script / update env command before commits.

A few useful git hooks to integrate with [pre-commit](http://pre-commit.com).

Check [Appendix E. Exit Codes With Special Meanings](http://www.tldp.org/LDP/abs/html/exitcodes.html)

### Using command-hook with pre-commit

Add this to your `.pre-commit-config.yaml`:

    -   repo: https://github.com/zonito/command-hook.git
        sha: ''  # Use the sha you want to point at
        hooks:
        -   id: command
            args: [--command, '<EXECUTE UNITTEST COMMAND BEFORE COMMIT>']
