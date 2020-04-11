# Android_Studio_Fragment

- 재사용을 위한 것. (부분화면, View, Layout(Activity))
- HTML의 common과 유사.
- 부분화면을 독립적으로 만들어주며 액티비티를 그대로 본떠 만든 것.
- 인텐트가 아닌 메소드 호출로 사용.
- 
- activity_main.xml 의 text

```java
<?xml version="1.0" encoding="utf-8"?>
<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:id="@+id/container"
        //id container는 MainFragment.xml의 id
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".MainActivity" >

    <fragment
        android:id="@+id/mainFragment"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:name="org.techtown.fragment.MainFragment" />

</FrameLayout>
```

- MainFragment.java

```java
package org.techtown.fragment;

import android.os.Bundle;

import androidx.fragment.app.Fragment;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;

public class MainFragment extends Fragment {

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // setContentView와 유사
        ViewGroup rootView = (ViewGroup) inflater.inflate(R.layout.fragment_main, container, false);

        Button button = rootView.findViewById(R.id.button);
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                MainActivity activity = (MainActivity) getActivity();
                activity.onFragmentChanged(1);
            }
        });

        return rootView;
    }
}

```

- MainActivity.java

```java
package org.techtown.fragment;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;

public class MainActivity extends AppCompatActivity {

    MainFragment mainFragment;

    MenuFragment menuFragment;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        mainFragment = (MainFragment) getSupportFragmentManager().findFragmentById(R.id.mainFragment);
//        mainFragment 변수를 getSupportFragmentManger로 참조, MainFragment 캐스팅
        menuFragment = new MenuFragment();
    }

    public void onFragmentChanged(int index) {
        if (index == 0) {
            getSupportFragmentManager().beginTransaction().replace(R.id.container, mainFragment).commit();
//            Transaction 여러개의 명령을 한꺼번에 실행할 때 사용,
        } else if (index == 1) {
            getSupportFragmentManager().beginTransaction().replace(R.id.container, menuFragment).commit();
        }
    }
}

```

- MenuFragment.java

```java
package org.techtown.fragment;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.fragment.app.Fragment;

public class MenuFragment extends Fragment {

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // setContentView와 유사
        return inflater.inflate(R.layout.fragment_menu, container, false);
    }
}

```

