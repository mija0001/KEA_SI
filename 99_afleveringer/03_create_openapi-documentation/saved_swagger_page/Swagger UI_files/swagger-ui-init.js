
window.onload = function() {
  // Build a system
  var url = window.location.search.match(/url=([^&]+)/);
  if (url && url.length > 1) {
    url = decodeURIComponent(url[1]);
  } else {
    url = window.location.origin;
  }
  var options = {
  "swaggerDoc": {
    "openapi": "3.0.0",
    "info": {
      "title": "Convert API",
      "version": "1.0.0",
      "description": "A simple API for converting units of length"
    },
    "paths": {
      "/api/convert": {
        "post": {
          "summary": "Convert from one unit of length to another",
          "requestBody": {
            "required": true,
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "from": {
                      "type": "string",
                      "description": "The unit to convert from",
                      "enum": [
                        "mm",
                        "cm",
                        "m",
                        "km",
                        "mi",
                        "ft",
                        "yd",
                        "in",
                        "nmi"
                      ]
                    },
                    "to": {
                      "type": "string",
                      "description": "The unit to convert to",
                      "enum": [
                        "mm",
                        "cm",
                        "m",
                        "km",
                        "mi",
                        "ft",
                        "yd",
                        "in",
                        "nmi"
                      ]
                    },
                    "amount": {
                      "type": "number",
                      "description": "The amount to convert"
                    }
                  }
                }
              }
            }
          },
          "responses": {
            "200": {
              "description": "The result of the conversion",
              "content": {
                "application/json": {
                  "schema": null,
                  "type": "object",
                  "properties": {
                    "result": {
                      "type": "number"
                    }
                  }
                }
              }
            },
            "400": {
              "description": "The request was invalid (e.g. missing parameters, invalid units, etc.)"
            }
          }
        }
      }
    },
    "components": {},
    "tags": []
  },
  "customOptions": {}
};
  url = options.swaggerUrl || url
  var urls = options.swaggerUrls
  var customOptions = options.customOptions
  var spec1 = options.swaggerDoc
  var swaggerOptions = {
    spec: spec1,
    url: url,
    urls: urls,
    dom_id: '#swagger-ui',
    deepLinking: true,
    presets: [
      SwaggerUIBundle.presets.apis,
      SwaggerUIStandalonePreset
    ],
    plugins: [
      SwaggerUIBundle.plugins.DownloadUrl
    ],
    layout: "StandaloneLayout"
  }
  for (var attrname in customOptions) {
    swaggerOptions[attrname] = customOptions[attrname];
  }
  var ui = SwaggerUIBundle(swaggerOptions)

  if (customOptions.oauth) {
    ui.initOAuth(customOptions.oauth)
  }

  if (customOptions.preauthorizeApiKey) {
    const key = customOptions.preauthorizeApiKey.authDefinitionKey;
    const value = customOptions.preauthorizeApiKey.apiKeyValue;
    if (!!key && !!value) {
      const pid = setInterval(() => {
        const authorized = ui.preauthorizeApiKey(key, value);
        if(!!authorized) clearInterval(pid);
      }, 500)

    }
  }

  if (customOptions.authAction) {
    ui.authActions.authorize(customOptions.authAction)
  }

  window.ui = ui
}
