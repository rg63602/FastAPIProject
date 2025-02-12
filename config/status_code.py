class StatusCode:
    """
    Centralized HTTP and custom business error codes for a large-scale production system.
    """

    # ✅ 🌍 1xx: Informational
    CONTINUE = 100
    SWITCHING_PROTOCOLS = 101
    PROCESSING = 102
    EARLY_HINTS = 103

    # ✅ 🎉 2xx: Success
    OK = 200
    CREATED = 201
    ACCEPTED = 202
    NON_AUTHORITATIVE_INFORMATION = 203
    NO_CONTENT = 204
    RESET_CONTENT = 205
    PARTIAL_CONTENT = 206
    MULTI_STATUS = 207
    ALREADY_REPORTED = 208
    IM_USED = 226

    # ✅ ⚠️ 3xx: Redirection
    MULTIPLE_CHOICES = 300
    MOVED_PERMANENTLY = 301
    FOUND = 302
    SEE_OTHER = 303
    NOT_MODIFIED = 304
    USE_PROXY = 305
    TEMPORARY_REDIRECT = 307
    PERMANENT_REDIRECT = 308

    # ✅ 🚨 4xx: Client Errors
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    PAYMENT_REQUIRED = 402
    FORBIDDEN = 403
    NOT_FOUND = 404
    METHOD_NOT_ALLOWED = 405
    NOT_ACCEPTABLE = 406
    PROXY_AUTHENTICATION_REQUIRED = 407
    REQUEST_TIMEOUT = 408
    CONFLICT = 409
    GONE = 410
    LENGTH_REQUIRED = 411
    PRECONDITION_FAILED = 412
    PAYLOAD_TOO_LARGE = 413
    URI_TOO_LONG = 414
    UNSUPPORTED_MEDIA_TYPE = 415
    RANGE_NOT_SATISFIABLE = 416
    EXPECTATION_FAILED = 417
    IM_A_TEAPOT = 418
    MISDIRECTED_REQUEST = 421
    UNPROCESSABLE_ENTITY = 422
    LOCKED = 423
    FAILED_DEPENDENCY = 424
    TOO_EARLY = 425
    UPGRADE_REQUIRED = 426
    PRECONDITION_REQUIRED = 428
    TOO_MANY_REQUESTS = 429
    REQUEST_HEADER_FIELDS_TOO_LARGE = 431
    UNAVAILABLE_FOR_LEGAL_REASONS = 451

    # ✅ 🔥 5xx: Server Errors
    INTERNAL_SERVER_ERROR = 500
    NOT_IMPLEMENTED = 501
    BAD_GATEWAY = 502
    SERVICE_UNAVAILABLE = 503
    GATEWAY_TIMEOUT = 504
    HTTP_VERSION_NOT_SUPPORTED = 505
    VARIANT_ALSO_NEGOTIATES = 506
    INSUFFICIENT_STORAGE = 507
    LOOP_DETECTED = 508
    NOT_EXTENDED = 510
    NETWORK_AUTHENTICATION_REQUIRED = 511

    # ✅ 🏆 6xx+: Custom Business-Specific Errors (Structured Ranges)

    # 🔹 460-469: User Errors
    USER_ERRORS = 460
    USER_NOT_FOUND = 461
    USER_ALREADY_EXISTS = 462
    USER_ACCESS_DENIED = 463
    USER_EMAIL_INVALID = 464
    USER_ALREADY_DELETED = 465
    USER_ALREADY_UPDATED = 466
    USER_ALREADY_REPORTED = 467
    USER_ALREADY_PUBLISHED = 468
    USER_ALREADY_UNPUBLISHED = 469

    # 🔹 470-479: Order Errors
    ORDER_ERRORS = 470
    ORDER_NOT_FOUND = 471
    PAYMENT_FAILED = 472
    ORDER_ALREADY_PROCESSED = 473
    INVALID_ORDER_STATUS = 474

    # 🔹 480-489: Invoice Errors
    INVOICE_ERRORS = 480
    INVOICE_NOT_FOUND = 481
    INVOICE_INVALID = 482
    INVOICE_ALREADY_PAID = 483

    # 🔹 490-499: Cart Errors
    CART_ERRORS = 490
    CART_EMPTY = 491
    ITEM_NOT_AVAILABLE = 492
    ITEM_QUANTITY_INVALID = 493

    # 🔹 500-509: Seller Errors
    SELLER_ERRORS = 500
    SELLER_NOT_FOUND = 501
    SELLER_UNAUTHORIZED = 502
    SELLER_ALREADY_EXISTS = 503

    # 🔹 510-519: Product Errors
    PRODUCT_ERRORS = 510
    PRODUCT_OUT_OF_STOCK = 511
    PRODUCT_INVALID_SKU = 512
    PRODUCT_DISCONTINUED = 513

    # 🔹 520-529: Filter Errors
    INVALID_FILTER_COLUMN = 520
    INVALID_FILTER_COLUMN_TYPE = 521
    INVALID_FILTER_COLUMN_VALUE = 522

    # 🔹 700-709: Rate Limit & Security
    RATE_LIMIT_EXCEEDED = 701
    UNAUTHORIZED_ACCESS = 702
