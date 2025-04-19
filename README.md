# AI Translator

A powerful Python library for accessing multiple translation services through a unified API.

## Table of Contents
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Core Features](#core-features)
- [Translation Services](#translation-services)
- [Language Detection](#language-detection)
- [API Reference](#api-reference)
- [Examples](#examples)
- [Error Handling](#error-handling)
- [Limitations](#limitations)

## Installation

```bash
pip install aitranslator
```

## Quick Start

```python
from aitranslator import Translator

# Initialize the translator
translator = Translator()

# Translate text from auto-detected language to English
result = translator.google("Привет, мир!", "en")
print(result['response']['translated_text'])  # Output: "Hello, world!"
```

## Core Features

- Access to 5 different translation services via a unified API
- Automatic language detection
- Support for specific source and target languages
- Error handling with appropriate HTTP status codes
- JSON response format for easy integration

## Translation Services

The library provides access to the following translation engines:

| Method | Service | Description |
|--------|---------|-------------|
| `google()` | Google Translate | Google's neural machine translation service |
| `deepl()` | DeepL | Highly accurate translation service known for natural-sounding results |
| `amazon()` | Amazon Translate | Amazon Web Services' neural machine translation service |
| `modern_mt()` | ModernMT | Adaptive neural machine translation |
| `libre()` | LibreTranslate | Open-source machine translation |

## Language Detection

The library includes automatic language detection which can be used both as a standalone feature and as part of the translation process.

```python
# Detect language
detection = translator.detect("こんにちは")
print(detection["data"]["language_probability"]["code"])  # Output: "ja"
```

## API Reference

### Translator Class

```python
Translator()
```

Initializes a new translator instance.

### Translation Methods

Each translation method follows the same signature:

```python
def method_name(text, target, source='auto')
```

- `text` (str): The text to translate
- `target` (str): Target language code (e.g., "en", "fr", "de")
- `source` (str, optional): Source language code. Defaults to 'auto' for automatic detection.

Returns a JSON object with translation results.

### Available Methods

#### Google Translate

```python
translator.google(text, target, source='auto')
```

#### DeepL

```python
translator.deepl(text, target, source='auto')
```

#### Amazon Translate

```python
translator.amazon(text, target, source='auto')
```

#### ModernMT

```python
translator.modern_mt(text, target, source='auto')
```

#### LibreTranslate

```python
translator.libre(text, target, source='auto')
```

#### Language Detection

```python
translator.detect(text)
```

- `text` (str): The text to analyze (only first 100 characters are used)

Returns a JSON object with detected language information.

## Examples

### Translating with Different Services

```python
translator = Translator()

# Original text
text = "La vie est belle"

# Translate with different services
google_result = translator.google(text, "en", "fr")
deepl_result = translator.deepl(text, "en", "fr") 
amazon_result = translator.amazon(text, "en", "fr")

print(f"Google: {google_result['response']['translated_text']}")
print(f"DeepL: {deepl_result['response']['translated_text']}")
print(f"Amazon: {amazon_result['response']['translated_text']}")
```

### Using Auto-Detection

```python
# The source language will be automatically detected
result = translator.google("Guten Tag", "en")
print(result['response']['translated_text'])  # Output: "Good day"
```

## Error Handling

The library uses the `raise_for_status()` method from the requests library to handle HTTP errors. If the translation service returns a non-200 response, an exception will be raised.

```python
try:
    result = translator.google("Hello world", "invalid_language_code")
except requests.exceptions.HTTPError as e:
    print(f"An error occurred: {e}")
```
