using System;
using System.Runtime.Serialization;

namespace LinearyStructures
{
    [Serializable]
    internal class StackUnderflowException : Exception
    {
        public StackUnderflowException()
        {
        }

        public string ToString()
        {
            return "Stack is empty";
        }

        public StackUnderflowException(string message) : base(message)
        {
        }

        public StackUnderflowException(string message, Exception innerException) : base(message, innerException)
        {
        }

        protected StackUnderflowException(SerializationInfo info, StreamingContext context) : base(info, context)
        {
        }
    }
}