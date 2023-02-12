using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class KnightingaleScript : MonoBehaviour
{

    public Rigidbody2D myRigidbody;
    // public float KGMove;
    
    // Start is called before the first frame update
    void Start()
    {
        speed = 5.0f;
    }

    // Update is called once per frame
    void Update()
    {
        horizontal = Input.GetAxisRaw("Horizontal");
        vertical = Input.GetAxisRaw("Vertical");
    }
}
