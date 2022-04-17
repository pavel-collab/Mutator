/*!
     \brief Euclide algorithm
     \param a,b 

     (Demonstration of code in the documentation block)

     Example code:
     \code
     int gcd(int a, int b) {
            int r;
            while (b) {
                  r = a % b;
                  a = b;
                  b = r;
            }
            return r;
     }
     \endcode
*/
int gcd(int a, int b);
