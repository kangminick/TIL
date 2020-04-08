# Android_Studio_Parcelable

- Class 객체 전달. (Intent)
- Task는 다른 프로세스의 (다른 App) Activity를 불러 올 수 있다.
- SimpleData라는 class를 생성.

```java
package org.techtown.parcelable;

import android.os.Parcel;
import android.os.Parcelable;

public class SimpleData implements Parcelable {
//    method가 구현이 안되면 위에 붉은 밑줄이 그어짐. generate로 해결

    int code;
    String message;

    public SimpleData(int code, String message) {
        this.code = code;
        this.message = message;
    }
//  주는 데이터

    public SimpleData(Parcel src) {
        code = src.readInt();
        message = src.readString();
    }
//    받는 데이터

    public static final Parcelable.Creator CREATOR = new Parcelable.Creator() {
        public SimpleData createFromParcel(Parcel in){
            return new SimpleData(in);
        }

        public SimpleData[] newArray(int size){
            return  new SimpleData[size];
        }
    };

    @Override
    public int describeContents() {
        return 0;
    }

    @Override
    public void writeToParcel(Parcel dest, int flags) {
        dest.writeInt(code);
        dest.writeString(message);
    }
}
```

- MainActivity

```java
package org.techtown.parcelable;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Button button = findViewById(R.id.button);
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(getApplicationContext(), MenuActivity.class);

                SimpleData data = new SimpleData(101, "ok");
                intent.putExtra("data", data);
                startActivity(intent);
            }
        });
    }
}
```

- MenuActivity

```java
package org.techtown.parcelable;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

public class MenuActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_menu);

        Button button = findViewById(R.id.button);
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                finish();
            }
        });

        Intent intent = getIntent();
        processIntent(intent);
    }

    public void processIntent(Intent intent) {
        if (intent != null){
            Bundle bundle = intent.getExtras();
            SimpleData = bundle.getParcelable("data");
            if (data != null) {
                Toast.makeText(this, "전달받은 객체 : " + data.code + "," + data.message, Toast.LENGTH_LONG).show();
            }
        }
    }
}
// 강의에서는 ProcessIntent안의 SimpleData, data가 제대로 참조 된거 같지만 내꺼에는 빨간줄 생김
```

