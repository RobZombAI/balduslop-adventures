package com.robzomb.gta.augusta

import android.annotation.SuppressLint
import android.app.Activity
import android.os.Build
import android.os.Bundle
import android.util.Log
import android.view.View
import android.view.WindowInsets
import android.view.WindowInsetsController
import android.view.WindowManager
import android.webkit.ConsoleMessage
import android.webkit.WebChromeClient
import android.webkit.WebResourceRequest
import android.webkit.WebResourceResponse
import android.webkit.WebSettings
import android.webkit.WebView
import android.webkit.WebViewClient

class MainActivity : Activity() {

    private lateinit var webView: WebView
    private val TAG = "GTA_Augusta"

    @SuppressLint("SetJavaScriptEnabled")
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        // Keep screen on during gameplay
        window.addFlags(WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON)

        webView = WebView(this)
        setContentView(webView)

        // Hide navigation and status bars for full immersion (after setContentView)
        hideSystemUI()

        configureWebView()

        // Load local offline assets via secure virtual domain (no CORS or origin:null limitations)
        webView.loadUrl("https://appassets.androidplatform.net/assets/www/index.html")

        // Handle back button smoothly (pause or open dialog instead of quitting abruptly)
        setupBackHandler()
    }

    @SuppressLint("SetJavaScriptEnabled")
    private fun configureWebView() {
        val settings = webView.settings
        settings.javaScriptEnabled = true
        settings.domStorageEnabled = true
        settings.databaseEnabled = true
        settings.allowFileAccess = true
        settings.allowContentAccess = true
        @Suppress("DEPRECATION")
        settings.allowFileAccessFromFileURLs = true
        @Suppress("DEPRECATION")
        settings.allowUniversalAccessFromFileURLs = true
        settings.mediaPlaybackRequiresUserGesture = false
        settings.cacheMode = WebSettings.LOAD_DEFAULT
        settings.loadsImagesAutomatically = true

        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.LOLLIPOP) {
            settings.mixedContentMode = WebSettings.MIXED_CONTENT_ALWAYS_ALLOW
        }

        // Hardware acceleration
        webView.setLayerType(View.LAYER_TYPE_HARDWARE, null)
        webView.isVerticalScrollBarEnabled = false
        webView.isHorizontalScrollBarEnabled = false

        val assetLoader = androidx.webkit.WebViewAssetLoader.Builder()
            .addPathHandler("/assets/", androidx.webkit.WebViewAssetLoader.AssetsPathHandler(this))
            .build()

        webView.webChromeClient = object : WebChromeClient() {
            override fun onConsoleMessage(consoleMessage: ConsoleMessage): Boolean {
                Log.d(TAG, "[WebView Console] ${consoleMessage.message()} -- line ${consoleMessage.lineNumber()} of ${consoleMessage.sourceId()}")
                return true
            }
        }

        webView.webViewClient = object : WebViewClient() {
            override fun shouldInterceptRequest(
                view: WebView,
                request: WebResourceRequest
            ): WebResourceResponse? {
                val urlStr = request.url.toString()
                if (urlStr.contains("/assets/assets/")) {
                    val fixedPath = "www/" + urlStr.substringAfter("/assets/")
                    try {
                        val stream = assets.open(fixedPath)
                        val mimeType = when {
                            urlStr.endsWith(".glb") -> "model/gltf-binary"
                            urlStr.endsWith(".js") -> "application/javascript"
                            urlStr.endsWith(".css") -> "text/css"
                            urlStr.endsWith(".png") -> "image/png"
                            urlStr.endsWith(".webp") -> "image/webp"
                            urlStr.endsWith(".mp3") -> "audio/mpeg"
                            urlStr.endsWith(".wav") -> "audio/wav"
                            else -> "application/octet-stream"
                        }
                        return WebResourceResponse(mimeType, "UTF-8", stream)
                    } catch (e: Exception) {
                        Log.w(TAG, "Failed fallback asset $fixedPath: ${e.message}")
                    }
                }
                return assetLoader.shouldInterceptRequest(request.url)
            }

            override fun shouldOverrideUrlLoading(view: WebView?, request: WebResourceRequest?): Boolean {
                return false
            }

            override fun onPageFinished(view: WebView?, url: String?) {
                super.onPageFinished(view, url)
                Log.i(TAG, "GTA Augusta page loaded successfully: $url")
            }
        }
    }

    private fun setupBackHandler() {
        // Intercept back key to toggle pause
        // Handled via onBackPressed
    }

    @Deprecated("Deprecated in Java")
    override fun onBackPressed() {
        // Dispatch ESC key to game canvas to open pause menu
        webView.evaluateJavascript(
            """
            (function() {
                var escEvent = new KeyboardEvent('keydown', {
                    code: 'Escape',
                    key: 'Escape',
                    keyCode: 27,
                    which: 27,
                    bubbles: true
                });
                window.dispatchEvent(escEvent);
            })();
            """.trimIndent(), null
        )
    }

    override fun onResume() {
        super.onResume()
        hideSystemUI()
        webView.onResume()
        webView.resumeTimers()
    }

    override fun onPause() {
        super.onPause()
        webView.onPause()
        webView.pauseTimers()
    }

    override fun onDestroy() {
        webView.destroy()
        super.onDestroy()
    }

    override fun onWindowFocusChanged(hasFocus: Boolean) {
        super.onWindowFocusChanged(hasFocus)
        if (hasFocus) {
            hideSystemUI()
        }
    }

    private fun hideSystemUI() {
        try {
            if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.R) {
                window.decorView.windowInsetsController?.let { controller ->
                    controller.hide(WindowInsets.Type.statusBars() or WindowInsets.Type.navigationBars())
                    controller.systemBarsBehavior = WindowInsetsController.BEHAVIOR_SHOW_TRANSIENT_BARS_BY_SWIPE
                }
            } else {
                @Suppress("DEPRECATION")
                window.decorView.systemUiVisibility = (
                    View.SYSTEM_UI_FLAG_IMMERSIVE_STICKY
                    or View.SYSTEM_UI_FLAG_LAYOUT_STABLE
                    or View.SYSTEM_UI_FLAG_LAYOUT_HIDE_NAVIGATION
                    or View.SYSTEM_UI_FLAG_LAYOUT_FULLSCREEN
                    or View.SYSTEM_UI_FLAG_HIDE_NAVIGATION
                    or View.SYSTEM_UI_FLAG_FULLSCREEN
                )
            }
        } catch (e: Exception) {
            Log.w(TAG, "hideSystemUI non-fatal error: ${e.message}")
        }
    }
}
