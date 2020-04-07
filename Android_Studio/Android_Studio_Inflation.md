# Android_Studio_Inflation

- xml과 Activity를 통해 어떻게 App에서 보여지는가.
- MainActivity.java의 아래 코드에 의해 경로 Res - layout - activity_main이라는 파일을 Inflation 해준다.

```java
setContentView(R.layout.activity_main);
```

- AndroidManifest.xml에서 Activity의 Activity의 순서 (main으로) 변경 가능

```java
<application
        android:allowBackup="true"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:roundIcon="@mipmap/ic_launcher_round"
        android:supportsRtl="true"
        android:theme="@style/AppTheme">
            //아래 순서변경
        <activity android:name=".MainActivity"></activity>
        <activity android:name=".MenuActivity">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />

                <category android:name="android.intent.category.LAUNCHER" />
                    //실행시 보여줌
            </intent-filter>
        </activity>
    </application>
```

- 부분화면(layout)을 만들어 보여줄 수 있다.

```java
package org.techtown.inflater;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.os.Bundle;
import android.text.Layout;
import android.view.LayoutInflater;
import android.view.View;
import android.widget.Button;
import android.widget.LinearLayout;
import android.widget.Toast;

public class MenuActivity extends AppCompatActivity {
    LinearLayout container;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_menu);

        container = findViewById(R.id.container);

        Button button2 = findViewById(R.id.button2);
        button2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                addLayout();
            }
        });
    }
    public void addLayout() {
        LayoutInflater inflater = (LayoutInflater) getSystemService(Context.LAYOUT_INFLATER_SERVICE);
//        LayoutInflater를 통해 Layout으로 형변환. getSystemService는 Inflate된 Layout이 계속 동작하게해줌.
        inflater.inflate(R.layout.sub1, container, true);
//        sub1이라는 xml을 container에 붙여넣어달라.

        Toast.makeText(this, "부분화면이 추가되었습니다.", Toast.LENGTH_LONG).show();
    }
}

```



