# Android_Studio_Fragment2

- Fragment와 FrameLayout 두개를 이용해서 이미지 변환
- MainActivity.java

```java
package org.techtown.fragment2;

import androidx.appcompat.app.AppCompatActivity;
import androidx.fragment.app.FragmentManager;

import android.os.Bundle;

public class MainActivity extends AppCompatActivity implements ImageSelectionCallback {

    ListFragment listFragment;
    ViewerFragment viewerFragment;

    int[] images = {R.drawable.img3, R.drawable.img4, R.drawable.img5};

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        FragmentManager manager = getSupportFragmentManager();
        listFragment = (ListFragment) manager.findFragmentById(R.id.listFragment);
        viewerFragment = (ViewerFragment) manager.findFragmentById(R.id.viewerFragment);
    }

    @Override
    public void onImageSelected(int position) {
        viewerFragment.setImageView(images[position]);
    }
}

```

- ListFragment.java

```java
package org.techtown.fragment2;

import android.content.Context;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;

public class ListFragment extends Fragment {
    ImageSelectionCallback callback;

    @Override
    public void onAttach(@NonNull Context context) {
        super.onAttach(context);

        if (context instanceof ImageSelectionCallback){
            callback  = (ImageSelectionCallback) context;
        }
    }

    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        ViewGroup rootView = (ViewGroup) inflater.inflate(R.layout.fragment_list, container, false);

        Button button = rootView.findViewById(R.id.button);
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                MainActivity activity = (MainActivity) getActivity();
                if (callback != null){
                    callback.onImageSelected(0);
                }
            }
        });

        Button button2 = rootView.findViewById(R.id.button2);
        button2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (callback != null){
                    callback.onImageSelected(1);
                }
            }
        });

        Button button3 = rootView.findViewById(R.id.button3);
        button3.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (callback != null){
                    callback.onImageSelected(2);
                }
            }
        });
        return rootView;
    }
}

```

- ImageSelectionCallback interface 생성

```java
package org.techtown.fragment2;

public interface ImageSelectionCallback {

    public void onImageSelected(int position);
}
// generate를 통해 생성.
```

- ViewerFragment.java

```java
package org.techtown.fragment2;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;

public class ViewerFragment extends Fragment {

    ImageView imageView;

    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        ViewGroup rootView = (ViewGroup) inflater.inflate(R.layout.fragment_viewer, container, false);

        imageView = rootView.findViewById(R.id.imageView);

        return rootView;
    }

    public void setImageView(int resId) {
        imageView.setImageResource(resId);
//        setImageResource에 이미지 Id를 넣어주면 이미지가 보인다.
    }
}

```

- activity_main.xml

```java
<FrameLayout
        android:layout_width="match_parent"
        android:layout_height="0dp"
        android:layout_weight="1">
        <fragment
            android:id="@+id/listFragment"
            android:layout_width="match_parent"
            android:layout_height="match_parent"
            android:name="org.techtown.fragment2.ListFragment" />

    </FrameLayout>

    <FrameLayout
        android:layout_width="match_parent"
        android:layout_height="0dp"
        android:layout_weight="1">
        <fragment
            android:id="@+id/viewerFragment"
            android:layout_width="match_parent"
            android:layout_height="match_parent"
            android:name="org.techtown.fragment2.ViewerFragment" />

    </FrameLayout>
    //fragment, name과 id 생성
```

