# Core Processing Methods

| Method                  | Usage |
|-------------------------|----------|
| `invoke()`              | Calls the model synchronously and returns a single response. |
| `ainvoke()`             | Calls the model asynchronously and returns a single response. |
| `batch()`               | Processes multiple inputs at once and returns responses in order. |
| `abatch()`              | Asynchronous version of `batch()` for handling multiple inputs. |
| `batch_as_completed()`  | Processes multiple inputs and returns responses as they complete (out of order). |
| `abatch_as_completed()` | Asynchronous version of `batch_as_completed()`, returning responses as they finish. |

✅ **Best for:** Standard synchronous or asynchronous calls and batch processing.

---

# Streaming Methods

| Method         | Usage |
|---------------|----------|
| `stream()`    | Streams output token-by-token for a single request. |
| `astream()`   | Asynchronous version of `stream()`, providing a continuous stream of responses. |
| `astream_events()` | Streams events related to processing, such as model responses and metadata. |

✅ **Best for:** Handling **real-time token streaming** (e.g., chat applications, live transcripts).

---

# Parsing & Configuration Methods

| Method                   | Usage |
|--------------------------|----------|
| `parse_result()`         | Parses a response from the model into a structured format. |
| `aparse_result()`        | Asynchronous version of `parse_result()`. |
| `configurable_fields()`  | Lists configurable fields that can be adjusted dynamically. |
| `configurable_alternatives()` | Defines multiple alternative configurations (e.g., different temperatures). |
| `bind()`                 | Pre-configures settings for future calls without modifying the original object. |
| `with_config()`          | Applies custom settings (e.g., temperature, retries, caching) dynamically. |

✅ **Best for:** Structuring responses, **dynamic configuration, and pre-setting model behaviors**.

---

# Error Handling & Retries

| Method         | Usage |
|---------------|----------|
| `with_retry()` | Automatically retries failed calls with exponential backoff. |
| `with_fallbacks()` | Specifies alternative models to use if the primary model fails. |

✅ **Best for:** **Ensuring reliability** in production systems by handling failures smoothly.

---

# Event Handling & Monitoring

| Method              | Usage |
|--------------------|----------|
| `with_listeners()`  | Adds event listeners (e.g., logs, callbacks) for monitoring sync operations. |
| `with_alisteners()` | Asynchronous version of `with_listeners()`, used for async event monitoring. |

✅ **Best for:** Logging, debugging, and **tracking model behavior over time**.

---

# Summary: When to Use Each Method

| Use Case                   | Best Methods |
|----------------------------|----------------|
| **Single request (sync)**  | `invoke()` |
| **Single request (async)** | `ainvoke()` |
| **Batch processing (sync)** | `batch()`, `batch_as_completed()` |
| **Batch processing (async)** | `abatch()`, `abatch_as_completed()` |
| **Streaming responses** | `stream()`, `astream()` |
| **Dynamic settings** | `with_config()`, `configurable_alternatives()` |
| **Error handling** | `with_retry()`, `with_fallbacks()` |
| **Event monitoring** | `with_listeners()`, `with_alisteners()` |

---

# 🚀 Which Method Should You Use?

- If you **need responses quickly** → Use `invoke()` or `ainvoke()`
- If you **process multiple inputs at once** → Use `batch()` or `abatch()`
- If you **want real-time output** → Use `stream()` or `astream()`
- If you **want reliability** → Use `with_retry()` or `with_fallbacks()`
- If you **need logging/debugging** → Use `with_listeners()` or `with_alisteners()`
- If you **want flexibility** → Use `configurable_alternatives()` or `with_config()`

