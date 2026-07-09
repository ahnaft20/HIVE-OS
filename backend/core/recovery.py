import time

def _sanitize(value):
    """
    Prevent agents from receiving None or invalid values.
    """
    if value is None:
        return ""
    if isinstance(value, str):
        return value.strip()
    if isinstance(value, (list, tuple, dict)):
        return value
    if isinstance(value, (int, float, bool)):
        return str(value)
    return str(value)


def execute_with_retry(
    agent_name,
    function,
    retries=3,
    delay=1,
    *args,
):
    # ---------- INPUT VALIDATION ----------
    safe_args = []
    for arg in args:
        safe_args.append(_sanitize(arg))
    last_error = None

    for attempt in range(retries):
        try:
            result = function(*safe_args)

            # ---------- OUTPUT VALIDATION ----------
            if result is None:
                return f"""
{agent_name}

No output was generated.

Continue the workflow using the available information.
"""

            if isinstance(result, str) and not result.strip():
                return f"""
{agent_name}

Returned an empty response.

Continue the workflow using the available information.
"""

            if isinstance(result, list) and len(result) == 0:
                return f"""
{agent_name}

Empty list returned.

Continue the workflow using the available information.
"""

            if isinstance(result, dict) and not result:
                return f"""
{agent_name}

Empty dictionary returned.

Continue the workflow using the available information.
"""

            return result

        except Exception as e:
            last_error = e
            print(
                f"[Recovery] {agent_name} failed. "
                f"Retry {attempt + 1}/{retries} "
                f"| Error: {e}"
            )
            # Exponential backoff
            time.sleep(delay * (attempt + 1))

    print(
        f"[Recovery] {agent_name} permanently failed after {retries} retries."
    )
    return f"""
{agent_name} FAILED

Reason:

{last_error}

Fallback:

Continue the remaining workflow using the available completed departments.

Do not terminate HIVE.
"""